import multiprocessing

def worker(parola, jobs, results):
    while True:
        try:
            file = jobs.get()
            result = trovata(parola, file)
            results.put(result)
        except FileNotFoundError as errore:
            print("Errore ", errore)
        finally:
            jobs.task_done()


def trovata(parola, file):
    flag = False
    fp = open(file, 'r+')
    lines = fp.readlines()
    for line in lines:
        if line.__contains__(parola):
            flag = True
            break

    if flag:
        result = (fp.tell(), file)
    else:
        result = (None, file)

    return result

# fatto
def create_processes(p: str, jobs, results, concorrenza: int):
    for _ in range(concorrenza):
        process = multiprocessing.Process(target=worker, args=(p, jobs, results))
        process.daemon = True
        process.start()

# fatto credo
def add_jobs(listaFile, jobs):
    i = 0
    for file in listaFile:
        jobs.put(file)
        i += 1
    return i

# fatto
def stampa(listaDiFile: list, p: str, concorrenza: int):
    canceled = False
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(p, jobs, results, concorrenza)
    todo = add_jobs(listaDiFile, jobs)

    try:
        jobs.join()
    except KeyboardInterrupt:  # May not work on Windows
        canceled = True

    i = 0
    while not results.empty():
        result = results.get_nowait()
        pos = result[0]
        file = result[1]

        if pos is not None:
            print("La parola {} appare nel file {} in posizione {}.".format(p, pos, file))
        else:
            print("La parola {} non appare nel file {}.".format(p, file))
#

def main():
    files = ["file1", "file2", "file3"]
    parola = "computer"

    stampa(files, parola, 2)


if __name__ == "__main__":
    main()
