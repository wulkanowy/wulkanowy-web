from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import APIKeyCookie
from starlette import status
from app import models, paths
import requests
from datetime import datetime
from cryptography.fernet import Fernet
import ast
from git import Repo
import re
import math

cookie_sec = APIKeyCookie(name="key")

router = APIRouter()

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


class Github: 
    repos = Repo(path='..')
    current_commit_hash = repos.head.commit.hexsha
    c_number_master = repos.git.rev_list("--count", "master")
    commit_author = repos.head.commit.author.name
    commit_date = repos.head.commit.committed_datetime.strftime("%d.%m.%Y %H:%M")
    commit_size = convert_size(repos.head.commit.size)
    cc = repos.head.commit.message
    current_commit = cc.rstrip()
    repo_url = repos.remote("origin").url
    repo_name = re.search(r"\/[a-zA-Z]+\/[a-zA-Z]+.*", str(repo_url)).group(0)
    repo_commit_number = repos.git.rev_list("--count", "master")
    repo_size = repos.git.count_objects("-H")
    current_branch = repos.active_branch.name
    c_number_current_branch = repos.git.rev_list("--count", "HEAD", current_branch)
    current_branch_url = (repo_url + "/tree/" + current_branch)
    if (int(c_number_current_branch) - int(c_number_master) > 0):
        current_branch_commit_number = int(c_number_current_branch) - int(c_number_master)
    else:
        current_branch_commit_number = int(c_number_master) - int(c_number_current_branch)

@router.get("/github")
def get_branch_name(repozi: str = Depends(Github)):
    response = {
        "repo_name": Github.repo_name[1:],
        "repo_link": Github.repo_url,
        "repo_commit_number": Github.repo_commit_number,
        "repo_size": Github.repo_size[13:],
        "branch_info":[
            {
                "active_branch": Github.current_branch,
                "active_branch_url": Github.current_branch_url,
                "active_branch_commit_number": Github.current_branch_commit_number,
            }
        ],
        "commit_info":[
            {
                "active_commit": Github.current_commit,
                "active_commit_hash_long": Github.current_commit_hash,
                "commit_author": Github.commit_author,
                "commit_date": Github.commit_date,
                "commit_size": Github.commit_size,
            }
        ],
    }
    return response