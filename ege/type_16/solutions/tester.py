import subprocess
import os
import sys

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def run_python_file(filename):
    """Запускает Python файл и возвращает его вывод"""
    try:
        result = subprocess.run([sys.executable, filename], 
                              capture_output=True, 
                              text=True, 
                              timeout=30,
                              cwd=os.path.dirname(os.path.abspath(__file__)))
        
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, f"Ошибка выполнения: {result.stderr.strip()}"
    
    except subprocess.TimeoutExpired:
        return False, "Таймаут: выполнение заняло более 30 секунд"
    except FileNotFoundError:
        return False, "Файл не найден"
    except Exception as e:
        return False, f"Неожиданная ошибка: {str(e)}"

def main():
    print(f"{Colors.BLUE}Запуск тестирования файлов 1.py - 20.py{Colors.END}")
    print("=" * 60)
    
    successful = 0
    total = 0
    
    for i in range(1, 21):
        filename = f"{i}.py"
        total += 1
        
        print(f"{Colors.BLUE}Запуск {filename}...{Colors.END}")
        
        success, output = run_python_file(filename)
        
        if success:
            print(f"{Colors.GREEN}✓ {filename}: {output}{Colors.END}")
            successful += 1
        else:
            print(f"{Colors.RED}✗ {filename}: {output}{Colors.END}")
        
        print("-" * 40)
    
    print(f"{Colors.BLUE}Результаты:{Colors.END}")
    print(f"{Colors.GREEN}Успешно: {successful}/{total}{Colors.END}")
    if successful < total:
        print(f"{Colors.RED}С ошибками: {total - successful}/{total}{Colors.END}")

if __name__ == "__main__":
    main()