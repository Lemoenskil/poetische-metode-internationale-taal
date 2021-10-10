# poetische-metode-internationale-taal

The project can be viewed [at the Heroku hosted site](https://poetische-metode-international.herokuapp.com/).

## Instructions for internationalization

Follow these steps for each translation you want to apply to the HTML:

1. Open the appropriate HTML file.
1. Navigate to the text you would like to create localizations (translations) for.
1. Select the current text and copy it to the clipboard using `Ctrl + C`, or to a text file so you can use it later.
1. Replace the text with a translation tag (the tag should describe the function of the text in the page), and _save the file_. E.g.,
   ```
   {% trans 'PropositionDescription' %}
   ```
1. Run the following from the command-line in the project root to detect the localization tag you just added (This updates the translation files named `locale/${language_code}/django.po for the supported languages):
   ```
   ./tools/update_translatables.sh
   ```
1. Open the updated translation files, starting with the original language.
1. Navigate to the translation added for your tag. E.g.,
   ```
   #: home/templates/index.html:117
   msgid "PropositionDescription"
   msgstr ""
   ```
1. Add the original text you copied before between the `msgstr` quotes, and _save the file_.
1. Navigate to the translation for the other translation files.
1. Add the translated text for what you copied before between the `msgstr` quotes, and _save the file_.
1. Once you have updated all translation files _AND_ everything is saved, run the following (This compiles the translations you just added so that they can be displayed by Django):
   ```
   ./tools/compile_translatables.sh
   ```
1. Test that everything works.
1. Once you are happy with the result, use Git to add, commit and push the changes.
