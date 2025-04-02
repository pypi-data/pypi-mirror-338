import cv2
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

import itertools
import numpy as np
import logging
import traceback
import gc

from transformers import SamModel, SamConfig, SamMaskDecoderConfig
from transformers.models.sam.modeling_sam import SamMaskDecoder, SamVisionConfig

logger = logging.getLogger(__name__)

class FinetunedSAM():
    '''a helper class to handle setting up SAM from the transformers library for finetuning
    '''
    def __init__(self, sam_model):
        try:
            logger.info(f"Loading SAM model from {sam_model}")
            self.model = SamModel.from_pretrained(sam_model)
            self.model.eval()
            logger.info("SAM model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading SAM model: {str(e)}")
            logger.error(traceback.format_exc())
            raise

    def get_model(self):
        return self.model
    
    def load_weights(self, weight_path, map_location=None):
        try:
            logger.info(f"Loading weights from {weight_path}")
            self.model.load_state_dict(torch.load(weight_path, map_location=map_location))
            logger.info("Weights loaded successfully")
        except Exception as e:
            logger.error(f"Error loading weights: {str(e)}")
            logger.error(traceback.format_exc())
            raise


class SAMCellModel:
    """Adapter for FinetunedSAM to match the original implementation"""
    
    def __init__(self, model_path=None):
        """
        Initialize the SAMCell model
        
        Parameters
        ----------
        model_path : str or Path
            Path to the SAMCell model weights
        """
        logger.info("Initializing SAMCellModel")
        # Force CPU to avoid CUDA threading issues on macOS
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info(f"Using device: {self.device}")
        
        self.model = None
        self.initialized = False
        
        # Try to load model if path is provided
        if model_path:
            self.load_model(model_path)
            
    def load_model(self, model_path):
        """
        Load the SAMCell model from a given path
        
        Parameters
        ----------
        model_path : str or Path
            Path to the SAMCell model weights
        
        Returns
        -------
        bool
            True if model loaded successfully, False otherwise
        """
        try:
            logger.info(f"Loading model from {model_path}")
            # Create the base model
            self.model = FinetunedSAM('facebook/sam-vit-base')
            self.model.load_weights(model_path, map_location=self.device)
            self.model.model.to(self.device)
            self.model.model.eval()
            self.initialized = True
            logger.info("Model successfully loaded")
            return True
            
        except Exception as e:
            logger.error(f"Error in load_model: {str(e)}")
            logger.error(traceback.format_exc())
            self.model = None
            self.initialized = False
            return False
    
    def is_initialized(self):
        """Check if model is initialized"""
        return self.initialized
    
    def get_model(self):
        """Get the underlying model"""
        if not self.initialized:
            logger.error("Model is not initialized. Call load_model first.")
            raise RuntimeError("Model is not initialized. Call load_model first.")
        return self.model
    
    def cleanup(self):
        """Clean up model resources"""
        if self.model is not None:
            try:
                logger.info("Cleaning up model resources")
                del self.model
                self.model = None
                self.initialized = False
                
                # Force garbage collection
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                
                logger.info("Model resources cleaned up")
            except Exception as e:
                logger.error(f"Error during cleanup: {str(e)}")
                logger.error(traceback.format_exc()) 