import sys

def process_line(line):
  return str(len(line)).zfill(3) + " " + line.replace('\n', '').replace('\r', '') + " " + str("python" in line)


def output_line(line):
  sys.stdout.write(line + '\n')


if __name__ == "__main__":
  for line in sys.stdin:
    output_line(process_line(line))
