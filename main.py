# main.py

from src.health_checker import HealthChecker

input_folder = "test_dataset"
output_file = "output.txt"
image_size = (224, 224)

def main():
    print("............. dataset cleaning started ..........")
    health_checker = HealthChecker(input_folder,output_file , image_size)
    health_checker.check_folders()

main()