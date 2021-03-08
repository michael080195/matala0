# Do pip install gitpython
# run with python check_submition.py hw-id.txt
import os , sys , subprocess , re , git
global commit,id,giturl,grade,total
def main():
    print("4 Test(0,1,2,3)\n")
    try:
        total = 4
        grade = 0
        hw = open(sys.argv[1],'r+').read().splitlines()
        repo_url = hw[0]
        commit_id = hw[1]
        repo_path = hw[2]
        if(os.path.exists(repo_path)):
            return print("Directory  "+ repo_path+" is already exists, so please delete it and run the command again")
        print(repo_path)
        repo = git.Repo.clone_from(repo_url, repo_path, no_checkout=True)
        repo.git.checkout(commit_id)
        # base dirs
        os.mkdir(repo_path+'/inputs')
        os.mkdir(repo_path+'/outputs')
        basedir = os.getcwd()+"/"+repo_path+"/"
        # test 0 check that there is 2 commits
        print("\nTest 0 (Check if there is two commits)" )
        commits = list(repo.iter_commits('HEAD'))
        if(len(commits)) ==2:
            print("Passed")
            passed = "True"
            grade+=1
        else:
            print("There is no 2 commits Exactly")
            passed = "False"
        if(type(passed)!=str):
            passed  = "False"
        f = open(basedir+"/outputs/Total.txt",'w+')
        f.write("Test0:"+passed)
        f.close()
        
    except Exception as e: 
        print(e)
    
 
    # test 1
    # check 5+6=11
    try:
        print("\nTest 1 (5+6=11)" )
        f = open(basedir+"/inputs/test1.txt",'w+')
        f.write("5\n6")
        f.close()
        command = "cd "+repo_path+" && python add.py < " +basedir+"/inputs/test1.txt" + " > "+basedir+"/outputs/test1.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test1.txt",'r+').read().splitlines()
        check  =re.findall(r'[0-9]+', f[0])
        if int(check[0])==11:
            grade+=1
            passed = "True"
            print("Passed")
        else:
            print("ERROR: 5+6=11 and your program wrote ",int(check[0]))   
            passed = "False"
        if(type(passed)!=str):
            passed  = "False"
        f = open(basedir+"/outputs/Total.txt",'a')
        f.write("\nTest1:"+passed)
        f.close()
    except Exception as e: 
        print(e)

        # test 2
        # check -2-10=-12
    try:
        print("\nTest 2 ((-2)+(-10)=(-12))" )
        f = open(basedir+"/inputs/test2.txt",'w+')
        f.write("-2\n-10")
        f.close()
        command = "cd "+repo_path+" && python add.py < " +basedir+"/inputs/test2.txt" + " > "+basedir+"/outputs/test2.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        a = ""
        h = open(basedir+"/outputs/test2.txt", 'r')
        content = h.readlines()
        for line in content: 
                print(line)
                if line.find("-12") != -1:
                    a=True
                    
                   
        
        if a==True:
            grade+=1
            print("Passed")
            passed="True"
        else:
            print("ERROR: -2-10=-12 and your program wrote ",int(check[0]))
            passed="False"
        if(type(passed)!=str):
            passed  = "False"
        f = open(basedir+"/outputs/Total.txt",'a')
        f.write("\nTest2:"+passed)
        f.close() 
    except Exception as e: 
        print(e)


    #test 3 - check helloworld.py exists
    try:
        print("\nTest 3 (Check helloworld.py)" )
        command = "cd "+repo_path+" && python helloworld.py > "+basedir+"/outputs/test3.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test3.txt",'r+').read().splitlines()
        if str(f[0]).lower().find("hello world") == -1:
            print("there is no hello world!")
            passed="False"
        else:
            grade+=1
            print("Passed")
            passed="True"
        if(type(passed)!=str):
            passed  = "False"
        f = open(basedir+"/outputs/Total.txt",'a')
        f.write("\nTest3:"+passed)
        f.write("\nTotal Grade:"+str((grade/total)*100))
        f.close()
    except Exception as e: 
        print(e)
    print("Total Grade",(grade/total)*100,"%")



if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you need write python check_submition.py hw-id.py while id is your id number")
