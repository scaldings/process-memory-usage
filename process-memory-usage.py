import psutil
import json


def get_processes():
    process_list = []
    total_memory = psutil.virtual_memory().total
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['name', 'memory_percent'])
            try:
                if float(process_info['memory_percent']) > 3:
                    memory = float(total_memory) / 100 * float(process_info['memory_percent'])
                    memory_mb = memory * pow(10, -6)
                    json_info = {
                        "name": f"{process_info['name']}",
                        "memory_usage": f"{int(memory_mb)}"
                    } 
                    process_list.append(json_info)
                    
            except:
                print('An error occured.')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list


def format_processes(processes: list):
    sorted_processes = sorted(processes, key=lambda procObj: procObj["memory_usage"], reverse=True)
    i = 1
    for process in sorted_processes:
        print(f'{i}. {process["name"]} - {process["memory_usage"]}MB')
        i += 1


if __name__ == "__main__":
    format_processes(get_processes())
