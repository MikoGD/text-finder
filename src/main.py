import sys
import os
import re
import codecs

def main():
  argv = sys.argv
  if (len(argv) != 2):
    return
  # END IF

  root = argv[1]

  write_contents = ""
  for x in os.walk(root):
    (path, dirnames, filenames) = x

    for filename in filenames:
      with codecs.open(f"{path}\\{filename}", "r", encoding="utf-8", errors="ignore") as file:
        line_numbers = ""
        for index, line in enumerate(file.readlines()):
          # if re.search("[^a-zA-Z]any[^a-zA-Z]", line) != None:
          if re.search("((^|\\s)|([^a-zA-Z]))(any)(($|\\s)|([^a-zA-Z]))", line) != None:
            line_numbers = line_numbers + f"Any at line {index + 1}\n"
        # END FOR

        if len(line_numbers) > 0:
            write_contents = write_contents + f"## {path}\\{filename}\n" + line_numbers + "\n\n"
        # END IF

    # END FOR
  # END FOR

  with open("results.md", "w") as write_file:
    write_file.write(write_contents);
# END WITH
# END main()

if __name__ == "__main__":
  main()
