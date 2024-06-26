# Start from the Gitpod workspace full image
FROM gitpod/workspace-python-3.12

USER root

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Add the Google Chrome repository
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

USER gitpod

# Add the Chrome as a path variable
ENV CHROME_BIN=/usr/bin/google-chrome

# Check if Chrome was installed successfully
RUN google-chrome --version

# Run this command to build image
# docker build -t my-python-chrome-image
