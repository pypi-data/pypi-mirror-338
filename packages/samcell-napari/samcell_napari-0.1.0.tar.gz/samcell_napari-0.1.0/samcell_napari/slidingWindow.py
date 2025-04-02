import cv2
import numpy as np
import logging

logger = logging.getLogger(__name__)

class SlidingWindowHelper:
    def __init__(self, crop_size: int, overlap_size: int):
        self.crop_size = crop_size
        self.overlap_size = overlap_size
        logger.info(f"SlidingWindowHelper initialized with crop_size={crop_size}, overlap_size={overlap_size}")

    def seperate_into_crops(self, img):
        """
        Split image into overlapping crops
        Note: Method name has a typo but kept for compatibility with original code
        """
        try:
            if img is None or img.size == 0:
                logger.error("Empty image provided to seperate_into_crops")
                return [], [], (0, 0, 0, 0)
                
            # Mirror the image such that the edges are repeated around the overlap region
            img_mirrored = cv2.copyMakeBorder(img, self.overlap_size, self.overlap_size, self.overlap_size, self.overlap_size, cv2.BORDER_REFLECT)
            logger.info(f"Mirrored image shape: {img_mirrored.shape}")

            # Get the image dimensions
            height, width = img_mirrored.shape

            # Initialize a list to store cropped images
            cropped_images = []
            orig_regions = []
            crop_unique_region = (self.overlap_size, self.overlap_size, self.crop_size - 2 * self.overlap_size, self.crop_size - 2 * self.overlap_size)

            for y in range(0, height, self.crop_size - self.overlap_size * 2):
                for x in range(0, width, self.crop_size - self.overlap_size * 2):
                    # Calculate crop boundaries
                    x_start = x
                    x_end = x + self.crop_size
                    y_start = y
                    y_end = y + self.crop_size

                    if x_end > width:
                        x_start = width - self.crop_size
                        x_end = width
                    if y_end > height:
                        y_start = height - self.crop_size
                        y_end = height

                    # Extract the crop with mirrored edges
                    crop = img_mirrored[y_start:y_end, x_start:x_end]

                    # Get the unique portion of the crop
                    orig_region = (x_start + self.overlap_size, y_start + self.overlap_size, self.crop_size - 2 * self.overlap_size, self.crop_size - 2 * self.overlap_size)

                    # Append the cropped image to the list
                    cropped_images.append(crop)
                    orig_regions.append(orig_region)
            
            logger.info(f"Created {len(cropped_images)} crops")
            return cropped_images, orig_regions, crop_unique_region
            
        except Exception as e:
            logger.error(f"Error in seperate_into_crops: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return [], [], (0, 0, 0, 0)
    
    # Add alias with correct spelling
    separate_into_crops = seperate_into_crops

    def combine_crops(self, orig_size, cropped_images, orig_regions, crop_unique_region):
        try:
            if not cropped_images or not orig_regions:
                logger.error("No crops provided to combine_crops")
                return np.zeros(orig_size, dtype=np.float32)
                
            logger.info(f"Combining {len(cropped_images)} crops into image of size {orig_size}")
            
            output_img = np.zeros(orig_size, dtype=np.float32)
            for i, (crop, region) in enumerate(zip(cropped_images, orig_regions)):
                try:
                    x, y, w, h = region
                    x -= self.overlap_size
                    y -= self.overlap_size
                    
                    # Skip invalid crops
                    if crop.shape[0] != self.crop_size or crop.shape[1] != self.crop_size:
                        logger.warning(f"Skipping crop {i} with invalid shape {crop.shape}")
                        continue
                        
                    # Extract unique region
                    if (crop_unique_region[0] + crop_unique_region[2] <= crop.shape[0] and 
                        crop_unique_region[1] + crop_unique_region[3] <= crop.shape[1]):
                        unique_region = crop[crop_unique_region[0]:crop_unique_region[0] + crop_unique_region[2], 
                                            crop_unique_region[1]:crop_unique_region[1] + crop_unique_region[3]]
                                            
                        # Ensure the region we're trying to paste is within bounds
                        if y >= 0 and x >= 0 and y+h <= output_img.shape[0] and x+w <= output_img.shape[1]:
                            output_img[y:y+h, x:x+w] = unique_region
                        else:
                            logger.warning(f"Crop {i} region ({y}:{y+h}, {x}:{x+w}) outside image bounds {output_img.shape}")
                    else:
                        logger.warning(f"Crop {i} too small for unique region extraction")
                        
                except Exception as e:
                    logger.error(f"Error processing crop {i}: {str(e)}")
                    
            return output_img
            
        except Exception as e:
            logger.error(f"Error in combine_crops: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return np.zeros(orig_size, dtype=np.float32) 