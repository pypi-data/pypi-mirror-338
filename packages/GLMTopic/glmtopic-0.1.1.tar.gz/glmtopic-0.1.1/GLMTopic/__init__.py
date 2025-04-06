import torch # type: ignore
from sklearn.preprocessing import normalize # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore
import pandas as pd # type: ignore
from tqdm import tqdm # type: ignore
import umap.umap_ as umap # type: ignore
import hdbscan # type: ignore
from zhipuai import ZhipuAI # type: ignore
import re
import sys
import os
import pandas as pd # type: ignore
import ast
import umap.umap_ as umap # type: ignore
import numpy as np # type: ignore
import plotly.graph_objects as go # type: ignore
import plotly.offline as pyo # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.cluster.hierarchy import linkage, dendrogram # type: ignore
from typing import Optional, List, Callable, Dict
from plotly.subplots import make_subplots # type: ignore
import jieba # type: ignore
from collections import Counter
from tqdm import tqdm # type: ignore
from wordcloud import WordCloud # type: ignore


def analyze_text_clusters(df, api_key, text_column='text', matryoshka_dim=1024, num_keywords=10, quiet=False, language_type="auto"):
    """
    Perform cluster analysis on text data and generate topics and keywords
    
    Parameters:
    df -- Input pandas DataFrame, must contain text column
    api_key -- ZhipuAI API key
    text_column -- Column name containing text data, default 'text'
    matryoshka_dim -- Truncated embedding dimension, default 1024
    num_keywords -- Number of keywords per topic, default 10
    quiet -- Whether to suppress progress messages, default False
    language_type -- Language for generated topics, default "auto" (auto-detect), can also be "chinese" or "english"
    
    Returns:
    A tuple containing two DataFrames:
    1. Full processed results (with original data and new columns)
    2. Aggregated results by cluster (with topic, keywords and count), sorted by count descending
    """
    if not quiet:
        print("Generating text embeddings...")
    model = SentenceTransformer('aspire/acge_text_embedding')
    sentences = df[text_column].tolist()
    embeddings = model.encode(sentences, normalize_embeddings=False)
    embeddings = embeddings[..., :matryoshka_dim]
    embeddings = normalize(embeddings, norm="l2", axis=1)
    df['embedding'] = embeddings.tolist()
    
    if not quiet:
        print("Reducing dimensions with UMAP...")
    umap_model = umap.UMAP(random_state=0)
    embedding_2d = umap_model.fit_transform(df['embedding'].values.tolist()) 
    
    if not quiet:
        print("Clustering with HDBSCAN...")
    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, min_samples=1)
    clusterer.fit(embedding_2d)
    if not quiet:
        print(f"Number of clusters found: {len(set(clusterer.labels_)) - (1 if -1 in clusterer.labels_ else 0)}")
        print(f"Number of noise points: {sum(clusterer.labels_ == -1)}")
    df['cluster'] = clusterer.labels_
    df = df[df['cluster'] != -1].copy()
    if not quiet:
        print(f"Number of points after removing noise: {len(df)}")
    
    # Initialize ZhipuAI client
    client = ZhipuAI(api_key=api_key)
    
    def generate_topic(text, number=num_keywords, language="auto"):
        system_message = "You are a helpful assistant that provides professional, accurate, and insightful advice."
        
        if language == "auto":
            # Auto-detect language (Chinese or English)
            if re.search(r'[\u4e00-\u9fa5]', text):  # If contains Chinese characters
                language = "chinese"
            else:
                language = "english"

        user_message = f"Please respond in the following strict format:\nTopic: topic content\nKeywords: keyword1,keyword2,...,keyword{number}\nNote: Keywords must come from the original text, topic content is your one-word summary of all generated keywords\nPlease respond in {language}: {text}"
        
        response = client.chat.completions.create(
            model="glm-4-long",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
        )
        return response.choices[0].message.content
    
    # Generate topics for each cluster
    if not quiet:
        print("Generating topics for each cluster...")
    labels = set(df['cluster'])
    df['topic'] = ""
    
    for label in tqdm(labels):
        cluster_df = df[df['cluster'] == label]
        cluster_text = ' '.join(cluster_df[text_column].values)
        try:
            response = generate_topic(cluster_text, num_keywords, language_type)
            df.loc[df['cluster'] == label, 'topic'] = response
        except Exception as e:
            print(f"Error generating topic for cluster {label}: {e}")
            df.loc[df['cluster'] == label, 'topic'] = f"Error: {str(e)}"
    
    # Extract keywords
    if not quiet:
        print("Extracting keywords...")
    def extract_topic(text):
        match = re.search(r'Topic:\s*(.+)', text)
        return match.group(1).strip() if match else ''

    def extract_keywords(text):
        match = re.search(r'Keywords:\s*([^\n]+)', text)
        if match:
            keywords = match.group(1).strip()
            keywords = re.sub(r'\s*,\s*', ',', keywords)  # Normalize comma spacing
            return keywords
        return ''
    
    df['keywords'] = df['topic'].apply(extract_keywords)
    df['topic'] = df['topic'].apply(extract_topic)
    
    # Simple output format
    if not df.empty and len(df) > 0:
        sys.stderr = open(os.devnull, 'w')  # Redirect warnings
        print(f"KEYWORDS:{df['keywords'].iloc[0]}")
        sys.stderr = sys.__stderr__  # Restore stderr
    
    # Generate cluster statistics
    if not quiet:
        print("Generating cluster statistics...")
    cluster_stats = df.groupby('cluster').agg({
        'topic': 'first',
        'keywords': 'first',
        text_column: 'count'
    }).reset_index()
    
    cluster_stats = cluster_stats.rename(columns={text_column: 'count'})
    cluster_stats = cluster_stats[['topic', 'keywords', 'count']]  # Keep only these columns
    
    # Sort by count descending
    cluster_stats = cluster_stats.sort_values('count', ascending=False)

    return df, cluster_stats

def generate_intertopic_map(
    file_path=None,
    output_filename="intertopic_map.html",
    topic_col=None,
    count_col='count',
    embedding_col='embedding',
    n_components=2,
    random_state=42,
    color_scale='Blues',
    title="Intertopic Distance Map",
    size_multiplier=1,
    opacity_inverse=True,
    auto_open=True,
    df=None
):
    """
    Generate intertopic distance visualization (using UMAP dimensionality reduction and Plotly)
    
    Parameters:
    file_path (str, optional): Path to data file (CSV format), ignored if df is provided
    df (pd.DataFrame, optional): Direct DataFrame input
    output_filename (str): Output HTML filename
    topic_col (str, optional): Topic name column name, default None
    count_col (str): Count column name, default 'count'
    embedding_col (str): Embedding vector column name, default 'embedding'
    n_components (int): UMAP reduction dimension, default 2
    random_state (int): Random seed, default 42
    color_scale (str): Color scheme, default 'Blues'
    title (str): Chart title, default "Intertopic Distance Map"
    size_multiplier (float): Point size scaling factor, default 1
    opacity_inverse (bool): Whether to invert opacity (larger points more transparent), default True
    auto_open (bool): Whether to automatically open generated HTML, default True
    
    Returns:
    tuple: (plotly.graph_objs._figure.Figure, pd.DataFrame) - Plotly figure and DataFrame used
    """

    # Data loading and preprocessing
    if df is None and file_path is not None:
        df = pd.read_csv(file_path)
    elif df is None:
        raise ValueError("Either file_path or df must be provided")
    
    # Check sufficient data
    if len(df) < 2:
        raise ValueError("Insufficient data points for visualization")
    
    # Check required columns
    required_columns = [count_col]
    if topic_col is not None:
        required_columns.append(topic_col)
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # If no embedding column, create simple 2D layout
    if embedding_col not in df.columns:
        coords = np.array([[i, 0] for i in range(len(df))])
    else:
        # Process embedding column
        df = df.dropna(subset=[embedding_col])
        try:
            if isinstance(df[embedding_col].iloc[0], str):
                df[embedding_col] = df[embedding_col].apply(ast.literal_eval)
        except:
            raise ValueError(f"Failed to parse embedding vectors, ensure '{embedding_col}' column format is correct")

        # Get embeddings
        embeddings = np.array(df[embedding_col].tolist())
        
        # For very small datasets, use PCA or cosine similarity
        if len(df) < 5:
            from sklearn.decomposition import PCA # type: ignore
            if len(df) == 2:
                coords = np.array([[0, 0], [1, 0]])
            else:
                pca = PCA(n_components=2)
                coords = pca.fit_transform(embeddings)
        else:
            # UMAP dimensionality reduction
            n_neighbors = min(len(df) - 1, 15)  # Adjust n_neighbors based on data size
            umap_model = umap.UMAP(
                n_components=n_components,
                random_state=random_state,
                n_neighbors=n_neighbors,
                min_dist=0.1,
                metric='cosine'
            )
            coords = umap_model.fit_transform(embeddings)

    # Calculate visualization parameters
    sizes = df[count_col].tolist()
    max_size = max(sizes) if sizes else 1
    min_size = 20  # Increased minimum point size
    
    # Opacity calculation
    if opacity_inverse:
        base = 1 / max_size if max_size != 0 else 1
        opacity = [max(0.5, 1 - (i * base)) for i in sizes]  # Increased minimum opacity
    else:
        opacity = [max(0.5, i / max_size) for i in sizes]

    # Generate topic labels
    if topic_col and topic_col in df.columns:
        topics = df[topic_col].astype(str).tolist()
    else:
        topics = [f"Topic {i+1}" for i in range(len(df))]

    # Create hover text
    hover_texts = [
        f"Topic: {topic}<br>Size: {size}<br>Keywords: {kw}"
        for topic, size, kw in zip(topics, sizes, df['keywords'])
    ]

    # Create visualization
    fig = go.Figure()
    
    # Add scatter plot
    marker_sizes = [max(min_size, s * size_multiplier) for s in sizes]
    fig.add_trace(go.Scatter(
        x=coords[:, 0],
        y=coords[:, 1],
        mode='markers+text',  # Add text labels
        marker=dict(
            size=marker_sizes,
            color=sizes,
            opacity=opacity,
            colorscale=color_scale,
            showscale=True,
            colorbar=dict(
                title="Topic Size",
                titleside="right"
            )
        ),
        text=topics,  # Show topic labels
        textposition="top center",  # Label position
        hovertext=hover_texts,
        hoverinfo='text'
    ))

    # Update layout settings
    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        xaxis_title="Dimension 1",
        yaxis_title="Dimension 2",
        template="plotly_white",
        showlegend=False,
        xaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor='black',
            mirror=True
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor='black',
            mirror=True
        ),
        plot_bgcolor='white',
        width=800,
        height=600,
        margin=dict(l=50, r=50, t=80, b=50)
    )

    return fig, df

def hierarchical_clustering_plot(
    df: pd.DataFrame,
    output_path: str = 'dendrogram.png',
    topic_col: str = 'topic',
    count_col: str = 'count',
    embedding_col: str = 'embedding',
    filter_keywords: Optional[List[str]] = None,
    top_n: Optional[int] = 40,
    label_truncate: int = 10,
    label_suffix: str = '...',
    cluster_method: str = 'ward',
    figsize: tuple = (20, 10),
    orientation: str = 'left',
    title: str = 'Hierarchical Clustering Dendrogram',
    xlabel: str = 'Distance',
    ylabel: str = 'Topics',
    dpi: int = 300,
    font_family: str = 'Arial Unicode MS',
    show_plot: bool = False
) -> plt.Figure:
    """
    Generate hierarchical clustering dendrogram
    
    Parameters:
    df -- Input DataFrame with clustering results
    output_path -- Output image path
    topic_col -- Topic column name
    count_col -- Count column name
    embedding_col -- Embedding vector column name
    filter_keywords -- Keywords to filter out
    top_n -- Show top N topics
    label_truncate -- Label truncation length
    label_suffix -- Truncation suffix
    cluster_method -- Clustering method
    figsize -- Image dimensions
    orientation -- Dendrogram orientation
    title -- Chart title
    xlabel -- X-axis label
    ylabel -- Y-axis label
    dpi -- Image resolution
    font_family -- Font family
    show_plot -- Whether to display plot
    
    Returns:
    matplotlib Figure object
    """
    try:
        # Data validation
        required_cols = [topic_col, count_col]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Data preprocessing
        df_plot = df.copy()
        filter_keywords = filter_keywords or ['Due to excessive text length']
        filter_condition = df_plot[topic_col].apply(
            lambda x: not any(kw in x for kw in filter_keywords))
        df_plot = df_plot[filter_condition]

        if top_n:
            df_plot = df_plot.sort_values(by=count_col, ascending=False).head(top_n)

        def truncate_label(text: str) -> str:
            return (text[:label_truncate] + label_suffix) if len(text) > label_truncate else text

        df_plot['plot_label'] = df_plot[topic_col].apply(truncate_label)

        if df_plot.empty:
            raise ValueError("Filtered data is empty")

        # Process embeddings
        if embedding_col not in df_plot.columns:
            n = len(df_plot)
            X = np.array([[i] for i in range(n)])  # Use 1D coordinates
        else:
            try:
                if isinstance(df_plot[embedding_col].iloc[0], str):
                    df_plot[embedding_col] = df_plot[embedding_col].apply(ast.literal_eval)
                X = np.array(df_plot[embedding_col].tolist())
            except Exception as e:
                raise ValueError(f"Embedding processing failed: {str(e)}")

        # Hierarchical clustering
        Z = linkage(X, method=cluster_method)

        # Create figure
        plt.rcParams['font.family'] = font_family
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
        
        # Draw dendrogram
        dendrogram(
            Z,
            labels=df_plot['plot_label'].tolist(),
            orientation=orientation,
            leaf_font_size=12,
            ax=ax
        )

        ax.set_title(title, fontsize=16)
        ax.set_xlabel(xlabel, fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        
        # Save image
        # plt.savefig(output_path, bbox_inches='tight', dpi=dpi)
        
        if show_plot:
            plt.show()
        else:
            plt.close(fig)  # Close if not showing
            
        return fig

    except Exception as e:
        plt.close()
        raise RuntimeError(f"Failed to generate clustering plot: {str(e)}") from e


def generate_topic_wordclouds(
    df: pd.DataFrame,
    output_dir: str = "wordclouds",
    text_column: str = "text",
    topic_col: str = "topic",
    keywords_col: str = "keywords",
    font_path: Optional[str] = None,
    stopwords_path: Optional[str] = None,
    extra_stopwords: Optional[set] = None,
    max_words: int = 200,
    top_keywords: int = 15,
    width: int = 800,
    height: int = 600,
    background_color: str = "white",
    quiet: bool = False,
    target_topics: Optional[List[str]] = None
) -> Dict[str, WordCloud]:
    """
    Generate topic wordclouds (returns visualization objects only)
    
    Parameters:
    df -- DataFrame containing text data
    output_dir -- Output directory
    text_column -- Text column name
    topic_col -- Topic column name
    keywords_col -- Keywords column name
    font_path -- Font file path (if None, will attempt to find a suitable Chinese font)
    stopwords_path -- Stopwords file path (if None, will look for package default)
    extra_stopwords -- Additional stopwords
    max_words -- Maximum words to display
    top_keywords -- Top keywords count
    width -- Image width
    height -- Image height
    background_color -- Background color
    quiet -- Silent mode
    target_topics -- Specific topics to process
    
    Returns:
    Dictionary {topic name: WordCloud object}
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Load stopwords
    stopwords = set()
    
    # Try to load stopwords from provided path
    if stopwords_path and os.path.exists(stopwords_path):
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            stopwords.update(f.read().splitlines())
    # If no path provided or file not found, try package default location
    elif stopwords_path is None:
        # Try to find the default stopwords file in the package
        default_path = os.path.join(os.path.dirname(__file__), 'data', 'hit_stopwords.txt')
        if os.path.exists(default_path):
            with open(default_path, 'r', encoding='utf-8') as f:
                stopwords.update(f.read().splitlines())
        else:
            if not quiet:
                print("Warning: Default stopwords file not found. Continuing without stopwords.")
    else:
        if not quiet:
            print(f"Warning: Stopwords file not found at {stopwords_path}. Continuing without stopwords.")
    
    if extra_stopwords:
        stopwords.update(extra_stopwords)
    
    # Find a suitable Chinese font if none is provided
    if font_path is None:
        possible_fonts = [
            # macOS fonts
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/STHeiti Light.ttc',
            '/System/Library/Fonts/STHeiti Medium.ttc',
            '/Library/Fonts/Microsoft/SimHei.ttf',
            '/Library/Fonts/Microsoft/SimSun.ttf',
            # Windows fonts
            'C:/Windows/Fonts/simhei.ttf',
            'C:/Windows/Fonts/simsun.ttc',
            'C:/Windows/Fonts/msyh.ttc',
            # Linux fonts
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            # Matplotlib default font
            os.path.join(os.path.dirname(plt.matplotlib_fname()), 'fonts/ttf/DejaVuSans.ttf')
        ]
        
        for font in possible_fonts:
            if os.path.exists(font):
                font_path = font
                if not quiet:
                    print(f"Using font: {font_path}")
                break
        
        if font_path is None and not quiet:
            print("Warning: No suitable Chinese font found. Text may not display correctly.")
    
    # Determine which topics to process
    if target_topics is None:
        topics = df[topic_col].unique().tolist()
    else:
        topics = [t for t in target_topics if t in df[topic_col].values]
    
    if not topics:
        raise ValueError("No available topic data")
    
    # Store wordcloud objects
    wordclouds = {}
    
    for topic in tqdm(topics, disable=quiet, desc="Generating wordclouds"):
        # Get topic-related text
        topic_texts = df[df[topic_col] == topic][text_column].tolist()
        combined_text = ' '.join(str(t) for t in topic_texts if pd.notna(t))
        
        # Word segmentation and frequency count
        words = [w for w in jieba.cut(combined_text) 
                if w.strip() and w not in stopwords and len(w) > 1]
        word_freq = Counter(words)
        
        # Enhance keyword weights
        topic_keywords = []
        for kw_str in df[df[topic_col] == topic][keywords_col].dropna():
            topic_keywords.extend(kw.strip() for kw in str(kw_str).split(',') if kw.strip())
        
        for kw in topic_keywords[:top_keywords]:
            if kw in word_freq:
                word_freq[kw] *= 3  # Increase keyword weight
        
        # Generate wordcloud
        try:
            wc = WordCloud(
                font_path=font_path,
                width=width,
                height=height,
                background_color=background_color,
                max_words=max_words,
                prefer_horizontal=0.9,
                scale=1.5,
                collocations=False,  # Avoid word repetitions
                mode='RGBA'  # Ensure transparent background for better visualization
            ).generate_from_frequencies(word_freq)
            
            wordclouds[topic] = wc
        except Exception as e:
            if not quiet:
                print(f"Error generating wordcloud for topic '{topic}': {str(e)}")
                
            # Try without custom font if font is the issue
            if "font" in str(e).lower() and font_path is not None:
                try:
                    if not quiet:
                        print("Retrying without custom font...")
                    wc = WordCloud(
                        width=width,
                        height=height,
                        background_color=background_color,
                        max_words=max_words,
                        prefer_horizontal=0.9,
                        scale=1.5,
                        collocations=False,
                        mode='RGBA'
                    ).generate_from_frequencies(word_freq)
                    
                    wordclouds[topic] = wc
                except Exception as e2:
                    if not quiet:
                        print(f"Second attempt failed: {str(e2)}")
    
    return wordclouds