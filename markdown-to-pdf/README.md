# OWASP Top Ten for LLMs - Markdown to PDF

The contents of this directory are used to generate the PDFs of translated versions of the OWASP Top Ten for LLMs using the md-to-pdf npm package.

## How to Contribute Translations

To contribute translations to the OWASP Top Ten for LLMs project, please follow these steps:

1. Fork this repository on GitHub by clicking on the "Fork" button at the top right corner of the repository page.

2. On your copy of this repo, create an ISO two-letter subdirectory in the `1_1_vulns` directory. This subdirectory should contain all the markdown files of the translation. You can match the same format as other languages.

3. Copy the Markdown files of the English version to your new directory and start translating. Make sure to follow the instructions in `_template.md` to ensure consistent styling. (There is no need to copy the _template.md file) The Markdown to PDF generator relies on this consistency.

4. Aim to replicate the translation as accurately as possible and avoid deviating from the original meaning of the Top Ten for LLMs.

5. In the `LLM00_Introduction.md` file, there is a section **About this translation**. You can add your name as a translator in this section.

6. Once the translation is complete, open a descriptive pull request to this repository to get it merged in.

7. There is no need to generate the PDF using the process in this document, but if you want to validate that your Markdown is in the correct format (and possibly add some styling if it needs tweaking), follow the instructions below.

8. If you are validating a translation, you can open an issue and tag the original translator to make the change. Once both the original translator and reviewer agree, you can open a pull request to this repository. (Remember to add your name to the About this translation section)

9. You should aim to keep a summary of the discussion around translations in the Github issue even if you were chatting in the OWASP Slack channel, which is located here: [OWASP Slack Channel](https://owasp.slack.com/archives/C063W2E791U).


## How to generate a Translated PDF

### Requirements
1. To generate PDFs from the markdown files you'll need to have the [md-to-pdf](https://www.npmjs.com/package/md-to-pdf) npm package installed globally. You can do this by installing globally if you have NPM installed on your machine:
```shell 
npm i -g md-to-pdf
```

2. You will require the translated Markdown files described above.

3. You will also need a CSS style file for the language in the `styles` directory. For languages based on latin characters you can copy the Portuguese file `topten-pt.css` as a starting point. 


### Descriptions of contents

- ``markdown-to-pdf/generated`` directory: This directory is where the PDFs are stored once they are generated. After the Markdown files are converted to PDF format, the resulting PDF files are placed in this directory for easy access and distribution.

- ``markdown-to-pdf/img`` directory: This directory is used to store all the images that will be included in the PDF files. When converting Markdown to PDF, any referenced images are typically embedded in the PDF document. The images are stored in this directory so that they can be easily referenced and included during the conversion process.

- ``markdown-to-pdf/styles`` directory: The styles directory contains custom CSS files for each language. When converting Markdown to PDF, the Markdown is first converted to HTML, and then the HTML is "printed" using Puppeteer to generate the PDF. The custom CSS files in the styles directory ensure that the PDFs have consistent styling and alignment, closely resembling the original Markdown files. Each language may have its own CSS file to handle language-specific formatting requirements.

- ``markdown-to-pdf/frontmatter.md``: This file serves as the configuration for Puppeteer, the tool used to generate the PDFs. It specifies how the PDFs should be generated and, importantly, defines the header and footer for each page of the PDF. The header and footer typically contain information such as page numbers, document title, and other relevant details. **It is crucial to note that on line 57 of frontmatter.md, the title is translated and needs to be changed before generating a PDF.** This ensures that the PDFs have the correct translated title.

- ``markdown-to-pdf/markdown_to_pdf.sh``: This file is responsible for executing the conversion process from Markdown to PDF. It contains the necessary commands and instructions to convert the Markdown files to PDF format using the md-to-pdf npm package. The usage of this file is typically explained in the project documentation or README file, providing step-by-step instructions on how to run the script and generate the PDFs.


### Usage

To generate PDFs from the markdown files, follow these steps:

1. Modify line 57 of `frontmatter.md` to show the correct title of the OWASP Top Ten in the appropriate language

2. Validate that the ISO code directory for the language exists in the `../1_1_vulns` directory and that the corresponding CSS file for the language exists in the `styles` directory.

3. Run the following command to generate the PDF:

	```shell
	./markdown_to_pdf.sh --language <language_iso_code>
	```

	Example

	```shell
	./markdown_to_pdf.sh --language pt
	```

	The generated PDF will be saved in generated directory with the ISO code as the filename. If a file already exists it will be overwritten. 

4. Validate that the contents of the file look similar to that of the main English file. 


### Options


- **Keep Markdown** If you add the ``--keep-markdown`` flag at the end, the script will not delete the temporary markdown file generated from all the cocatenated ones. Please note that the temporary file is located in ``./generated/tmp``. eg:
	```shell
	./markdown_to_pdf.sh --language pt --keep-markdown
	```



## License

This project is licensed under the terms of the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
