# Link
https://github.com/xm1k3/cent

# Download

```
GO111MODULE=on go get -u github.com/xm1k3/cent
go install github.com/xm1k3/cent@latest
```

# Download && Update templates

```
cent -p cent-nuclei-templates -k
cent update -p cent-nuclei-templates -d
```

# Usage

```
nuclei -l hosts.txt -t ./cent-nuclei-templates | anew NucleiScan_Publics
```
