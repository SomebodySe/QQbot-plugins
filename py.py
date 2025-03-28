import subprocess

def py(msgx):
    msg = msgx.split("/py", 1)[1].strip()
    filename = "src/plugins/run.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(msg)
    try:
        result = subprocess.check_output(["python3", filename], text=True, timeout=5).strip()
    except subprocess.TimeoutExpired:
        return("运行超时")
    if len(result) > 1000:
        return result[-1000:]
    elif result == "":
        return "无输出"
    else:
        return result
