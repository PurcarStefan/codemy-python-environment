import subprocess

def main():
    commit_and_push()
    print("Toate modificările au fost salvate. Puteți închide în siguranță browserul.")
    print("Codespace-ul se va opri automat după inactivitate.")

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8'), process.returncode

def commit_and_push():
    status_output, status_error, status_code = run_command("git status --porcelain")

    if status_code != 0:
        print(f"Eroare la verificarea statusului: {status_error}")
        return

    if not status_output:
        print("Nu sunt modificări de salvat.")
        return

    print("Adăugare modificări...")
    run_command("git add .")

    print("Creare commit...")
    run_command('git commit -m "Salvare automată la închidere"')

    print("Push către repository...")
    output, error, returncode = run_command("git push")

    if returncode != 0:
        print(f"Eroare la push: {error}")
    else:
        print(output)
        print("Push realizat cu succes!")



if __name__ == "__main__":
    main()