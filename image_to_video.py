import imageio
import os

# Specify the output video filename
output_video = 'output_video.mp4'

# Specify the directory where your images are stored
image_dir = './Semi_translation/results/shinkai-test/test_Shinkai/images/fake_B/'  # Adjust to your path

# Get all image filenames in the directory and sort them
image_filenames = sorted([img for img in os.listdir(image_dir) if img.endswith('.png')],
                         key=lambda x: int(x.split('_')[1].split('.')[0]))  # Sort by frame number

# Read the first image to get the dimensions
first_frame = imageio.imread(os.path.join(image_dir, image_filenames[0]))
height, width, _ = first_frame.shape

# Create a video writer object
with imageio.get_writer(output_video, fps=20) as writer:  # Set desired FPS
    for filename in image_filenames:
        image_path = os.path.join(image_dir, filename)
        frame = imageio.imread(image_path)
        writer.append_data(frame)

print(f'Video saved as {output_video}')
