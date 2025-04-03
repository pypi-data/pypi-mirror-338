import streamlit as st
from PIL import Image
import torch
import os
import sys
import logging
import subprocess
import pkg_resources
import streamlit.web.bootstrap as bootstrap
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_clip():
    """Ensure CLIP is installed from GitHub"""
    try:
        # Check if CLIP is installed
        pkg_resources.get_distribution('clip')
        
        # Try importing to verify it's the correct version
        try:
            import clip
            if not hasattr(clip, 'available_models'):
                logger.info("Reinstalling CLIP from GitHub...")
                subprocess.check_call([
                    sys.executable, "-m", "pip", "uninstall", "-y", "clip"
                ])
                raise ImportError
        except ImportError:
            logger.info("Installing CLIP from GitHub...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "git+https://github.com/openai/CLIP.git"
            ])
            import clip
        
        return clip
    except (pkg_resources.DistributionNotFound, ImportError):
        logger.info("Installing CLIP from GitHub...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "git+https://github.com/openai/CLIP.git"
        ])
        import clip
        return clip

# Initialize CLIP model with better error handling
@st.cache_resource
def load_model():
    try:
        clip = ensure_clip()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {device}")
        
        model, preprocess = clip.load("ViT-B/32", device=device)
        model.eval()
        return model, preprocess, device
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        st.error(f"Failed to load CLIP model: {str(e)}")
        return None, None, "cpu"

def run_app():
    """Entry point for the application when used as a package."""
    base_path = Path(__file__).parent / "base.py"
    args = []
    
    # Set up Streamlit command line arguments
    sys.argv = ["streamlit", "run", str(base_path)]
    
    # Run the Streamlit app
    bootstrap.run(str(base_path), '', args, {})

if __name__ == "__main__":
    run_app()