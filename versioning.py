import os

def version_commit():
    command1 = "git config --local user.name "+os.environ['USERNAME']
    os.system(command1)
    os.system('git add VERSION')
    os.system('git commit -m "Updated VERSION"')
    os.system('git push')
    print("VERSION successfully updated")

old_version=open("VERSION").read()
oldver_values = (open("VERSION").read().split("."))

sem_ver = {
    "major": oldver_values[0],
    "feat": oldver_values[1],
    "fix": oldver_values[2]
}


if "major" in os.environ['CUR_NAME']:
    sem_ver["major"] = str(int(oldver_values[0])+1)
    sem_ver["feat"] = '0'
    sem_ver["fix"] = '0'
elif "feat" in os.environ['CUR_NAME']:
    sem_ver["feat"] = str(int(oldver_values[1])+1)
elif "fix" in os.environ['CUR_NAME']:
    sem_ver["fix"] = str(int(oldver_values[2])+1)
new_version = sem_ver.get("major")+"." + \
    sem_ver.get("feat")+"."+sem_ver.get("fix")
file = open("VERSION", "r+")
file.truncate(0)
file.write(new_version)
file.close()
version_commit()
print("Version Changed from ",old_version," to ",new_version)
