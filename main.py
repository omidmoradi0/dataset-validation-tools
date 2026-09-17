from src.health_checker import healthChecker

input_folder = "test_dataset"
output_file = "output.txt"
image_size = (224, 224)

health_checker = healthChecker(input_folder,output_file)
print(health_checker.check_folders())