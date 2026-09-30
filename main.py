# main.py

from src.health_checker import HealthChecker

input_folder = "test_dataset"
output_file = "output.txt"
image_size = (224, 224)

def main():
    print("............. dataset cleaning started ..........")
    is_clear = int(input("do you want to clear output file (0:No | 1:Yes):"))
    if is_clear:
        open(output_file, 'w').close()
        
    health_checker = HealthChecker(input_folder,output_file , image_size)
    health_checker.check_folders()

main()