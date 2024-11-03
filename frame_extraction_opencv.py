from PIL import Image
import imageio

# Load the video
reader = imageio.get_reader('/home/23n0462/Scenimefy/original_videos/5.mp4')

# Get the frame rate of the video
fps = reader.get_meta_data()['fps']
print(f"Frame Rate: {fps} FPS")

# Set the desired frames per second for extraction
desired_fps =  18 # Change this to your desired FPS
frame_interval = int(fps / desired_fps)  # Calculate how many frames to skip

# Loop through each frame and save it as an image at the specified frame interval
for i, frame in enumerate(reader):
#     if i % frame_interval == 0:  # Save every nth frame based on the desired FPS
        image = Image.fromarray(frame)
        image.save(f"./Semi_translation/datasets/Sample/testA/frame_{i}.png")

# Close the reader
reader.close()
