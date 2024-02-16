import subprocess

url = "https://www.google.com"
url2 = "https://www.fast.com"

try:
    subprocess.run(["start", url], shell=True)
    subprocess.run(["start", url2], shell=True)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("funnciona")    