import subprocess

def main():
    commit_and_push()
    print("Toate modificările au fost salvate. Puteți închide în siguranță browserul.")
    print("Codespace-ul se va opri automat după inactivitate.")

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

def commit_and_push():
    print("Adăugare modificări...")
    run_command("git add .")

    print("Creare commit...")
    run_command('git commit -m "Salvare automată la închidere"')

    print("Push către repository...")
    _, error = run_command("git push")

    if error:
        print(f"Eroare la push: {error}")
    else:
        print("Push realizat cu succes!")

if __name__ == "__main__":
    main()