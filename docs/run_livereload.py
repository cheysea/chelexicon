from livereload import Server, shell
import os
import sys

if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f"Current Directory: {script_directory}")

    server = Server()
    server.watch('*.rst', shell('make html'), delay=1)
    server.watch('*.md', shell('make html'), delay=1)
    server.watch('*.py', shell('make html'), delay=1)
    server.watch('_static/*', shell('make html'), delay=1)
    server.watch('_templates/*', shell('make html'), delay=1)
    server.watch('../*.py', shell('make html'), delay=1)
    server.serve(root='_build/html')

