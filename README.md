# poetische-metode-internationale-taal

The project can be viewed [at the Heroku hosted site](https://poetische-metode-international.herokuapp.com/).

## Heroku set-up

To support audio files, additional non-python dependencies need to be installed. To be able to do so, you need to install [heroku-buildpack-apt](https://github.com/heroku/heroku-buildpack-apt) once when setting up a new Heroku deployment:

1. On the command-line, set your heroku app variable. E.g.:
   ```
   export HEROKU_APP=poetische-metode-international
   ```
1. Run the heroku `apps` command to start a session and log in:
   ```
   heroku apps
   ```
   The output will be one of the following: following:see the following output, unless you are already logged in, in which case you can skip the rest of this step:
   * If you are already logged in, just continue with the remaining steps:
     ```
     === Collaborated Apps
     ...
     ```
   * If you are not logged in, press any key as instructed, and log in via the browser window that opens:
     ```
     heroku: Press any key to open up the browser to login or q to exit: 
     Opening browser to https://cli-auth.heroku.com/auth/cli/browser/...
     ```
     On successful login, you should get the following output:
     ```
     Logging in... done
     ```
1. Install the [heroku-buildpack-apt](https://github.com/heroku/heroku-buildpack-apt):
   ```
   heroku buildpacks:add --index 1 heroku-community/apt
   ```
   If successful, you should get the following output:
   ```
   Buildpack added. Next release on poetische-metode-international will use:
     1. heroku-community/apt
     2. heroku/python
   ```

You will also have to install these dependencies on your Ubuntu development environment if you want to test locally:
```
sudo apt install libsox-fmt-mp3 libsox-fmt-all mpg321 dir2ogg ffmpeg
```

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
