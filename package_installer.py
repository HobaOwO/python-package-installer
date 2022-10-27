import subprocess

package = input("Enter package name: ")

subprocess.call(f"pip install {package}")




