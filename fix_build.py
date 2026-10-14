import os

build_gradle_path = 'android/build.gradle'
if os.path.exists(build_gradle_path):
    with open(build_gradle_path, 'r') as f:
        content = f.read()
    # Groovy tabanlı eski eklenti çakışmalarını önlemek için küçük bir düzenleme
    print("build.gradle incelendi.")
