import sys
import re
import settings


def insert_in_html_file(title: str, body_content: str) -> str:
    return (f"""<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
{body_content}
</body>
</html>""")


def check_file_extention(file_name: str) -> None:
    lst = re.findall(".template$", file_name)
    if (not lst):
        print("Error: file extention not supported")
        sys.exit()


def create_html_cv(template_replaced_content: str) -> None:
    try:
        cv_file = open("myCv.html", mode="w")
        cv_file.write(template_replaced_content)
    except OSError as ferror:
        print("Could not open file:", ferror)
        sys.exit()
    finally:
        cv_file.close()


def replace_patterns(content: list[str], variables: dict) -> list[str]:
    replaced_content: str = content
    for var in variables:
        replaced_content = replaced_content.replace(var, variables[var])
    replaced_content = insert_in_html_file(variables['{title}'],
                                           replaced_content)
    return (replaced_content)


def read_template_content(template_name: str) -> str:
    try:
        template_file = open(template_name, mode='r')
        line = template_file.readline()
        template_content: str = ""
        while True:
            if line == '':
                break
            template_content += line
            line = template_file.readline()
    except OSError as ferror:
        print("Could not open file:", ferror)
        sys.exit()
    finally:
        template_file.close()
    return (template_content)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 render.py [template_file_name]")
    else:
        check_file_extention(sys.argv[1])
        variables_name = [var for var in dir(settings)
                          if not var.startswith("__")]
        variables: dict = {}
        for var in variables_name:
            variables.update({'{' + var + '}': getattr(settings, var)})
        line = "hello {name}"
        for i in variables:
            line = line.replace(i, variables[i])
        template_content = read_template_content(sys.argv[1])
        replaced_content = replace_patterns(template_content, variables)
        create_html_cv(replaced_content)
