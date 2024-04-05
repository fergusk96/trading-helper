    #!/bin/sh

    # Decrypt the file
    mkdir $GITHUB_WORKSPACE/secrets
    # --batch to prevent interactive command --yes to assume "yes" for questions
    gpg --quiet --batch --yes --decrypt --passphrase="$DECRYPTION_KEY" \
    --output $GITHUB_WORKSPACE/secrets/credentials.json credentials.json.gpg
