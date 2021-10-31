from os import walk, system, makedirs
import shutil

def genSubjectHtml(folder, title, outputDir):
    title_safe = title.lower().replace(" ", "_").replace("'", "")

    makedirs(f"../{outputDir}/{title_safe}", exist_ok=True)

    _, _, filenames = next(walk(f'../{folder}'))

    filenames_md  = [filename for filename in filenames if filename.endswith(".md")]
    filenames_svg = [filename for filename in filenames if filename.endswith(".svg") or filename.endswith(".png")]
    filenames_md.sort()

    output = f"---\ntitle: {title}\n---\n\n"

    for filename in filenames_md:
        with open(f"../{folder}/{filename}", "r") as f:
            if "toc" in filename:
                continue
            file_title = f.readlines()[1].strip().split(": ")[1]
            file_title_safe = file_title.lower().replace(" ", "_").replace("'", "")
            output += f"[{file_title}]({file_title_safe}.html)\n"
            system(f"pandoc ../{folder}/{filename} -M category='{title}' --template=template.template -s --katex -o ../{outputDir}/{title_safe}/{file_title_safe}.html")

    system(f"pandoc --template=template.template -s -o ../{outputDir}/{title_safe}/index.html <<< \"{output}\"")

    for filename in filenames_svg:
        shutil.copyfile(f"../{folder}/{filename}",
                        f"../{outputDir}/{title_safe}/{filename}")

def genMainTOC(subjects, outputDir):
    output = f"---\ntitle: Table of Contents\n---\n\n"
    for subject, title in subjects.items():
        title_safe = title.lower().replace(" ", "_").replace("'", "")
        output += f"[{title}]({title_safe})\n"

    system(f"pandoc --template=template.template -M custom-toc=yes -s -o ../{outputDir}/index.html <<< \"{output}\"")

def main():
    folders = {
        'math': 'Calculus',
        'aleph/linear': 'Linear Algebra',
        'aleph/discrete': 'Discrete Mathematics',
        'aleph/methods': 'Mathematical Methods'
    }

    outputDir = 'docs'

    system(f"rm -rf ../{outputDir}/*")

    for folder, title in folders.items():
        genSubjectHtml(folder, title, outputDir)

    genMainTOC(folders, outputDir)

    shutil.copyfile("style.css", f"../{outputDir}/style.css")
    shutil.copyfile("divider.svg", f"../{outputDir}/divider.svg")
    shutil.copyfile("favicon.png", f"../{outputDir}/favicon.png")


if __name__ == "__main__":
    main()
