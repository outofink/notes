from os import walk, system, makedirs
import shutil

def genSubjectHtml(folder, outputDir):

    makedirs(f"../{outputDir}/{folder}", exist_ok=True)

    _, _, filenames = next(walk(f'../{folder}'))

    filenames_md  = [filename for filename in filenames if filename.endswith(".md")]
    filenames_svg = [filename for filename in filenames if filename.endswith(".svg")]
    filenames_md.sort()

    output = f"---\ntitle: {folder.title()}\n---\n\n"

    for filename in filenames_md:
        with open(f"../{folder}/{filename}", "r") as f:
            if "toc" in filename:
                continue
            title = f.readlines()[1].strip().split(": ")[1]
            title_safe = title.lower().replace(" ", "_").replace("'", "")
            output += f"[{title}]({title_safe}.html)\n"
            system(f"pandoc ../{folder}/{filename} -M category={folder.title()} --template=template.template -s --katex -o ../{outputDir}/{folder}/{title_safe}.html")

    system(f"pandoc --template=template.template -s -o ../{outputDir}/{folder}/index.html <<< \"{output}\"")

    for filename in filenames_svg:
        shutil.copyfile(f"../{folder}/{filename}",
                        f"../{outputDir}/{folder}/{filename}")

def genMainTOC(subjects, outputDir):
    output = f"---\ntitle: Table of Contents\n---\n\n"
    for subject in subjects:
        output += f"[{subject.title()}]({subject})\n"

    system(f"pandoc --template=template.template -M custom-toc=yes -s -o ../{outputDir}/index.html <<< \"{output}\"")

def main():
    folders = ['math']
    outputDir = 'docs'

    system(f"rm -rf ../{outputDir}/*")

    for folder in folders:
        genSubjectHtml(folder, outputDir)

    genMainTOC(folders, outputDir)

    shutil.copyfile("style.css", f"../{outputDir}/style.css")
    shutil.copyfile("divider.svg", f"../{outputDir}/divider.svg")
    shutil.copyfile("favicon.png", f"../{outputDir}/favicon.png")


if __name__ == "__main__":
    main()
