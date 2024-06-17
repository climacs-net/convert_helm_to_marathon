version: 2
plan:
  project-key: DEMO
  key: CONVERT
  name: Convert Helm to Marathon JSON

stages:
  - name: Build and Convert
    jobs:
      - job:
          key: BUILD
          name: Build and Convert
          tasks:
            - script:
                description: Extract and Convert Helm to Marathon JSON
                scriptBody: |
                  python3 convert_helm_to_marathon.py

  - name: Package and Upload
    jobs:
      - job:
          key: PACKAGE
          name: Package and Upload
          tasks:
            - script:
                description: Package the Converted Files
                scriptBody: |
                  tar -czvf converted_chart.tgz marathon.json

            - script:
                description: Upload to Nexus
                scriptBody: |
                  curl -u bamboonexus:VhaG0ng51mplengpASS \
                  -T converted_chart.tgz \
                  http://nexusdemo.climacs.net:8081/repository/bamboodemo/ \
                  -v
