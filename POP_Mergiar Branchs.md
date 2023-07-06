## Procedimento Operacional Padrão

##### Tenho novos arquivos e pastas criadas no meu repositório local. Como separar estas informações numa branch e subir no GitHub Remoto?

---

<div> 1 - thime@ (main)

 $ git status // este comando verifica o status das minhas modificações
 On branch main
 Your branch is up to date with 'origin/main'.

 Untracked files: (use "git add <file>..." to include in what will be committed)

 nothing added to commit but untracked files present (use "git add" to track)

---

</div>

<div> 2 - thime@ ../Estudos-Python (main)
 
 $ git checkout -b feat/CFD // este comando direciona você para a branch que deseja trabalhar
 Switched to a new branch 'feat/CFD'

thime@ (feat/Updates) // repare que agora você está na branch que criou

---

thime@ ../Estudos-Python (feat/Updates)
$ git branch
  feat/CFD
  feat/Updates // este item provavelmente estará marcado com "verde"
  main

---

thime@ ../Estudos-Python (feat/Updates)
$ git add . // este comando atualiza, adiciona, tudo que foi alterado ou excluído no repositório local na branch Updates

---

thime@ ../Estudos-Python (feat/Updates)
$ git commit -m"Branch Updates: organização dos arquivos"
[feat/Updates 20d0747] Branch Updates: organização dos arquivos
 7 files changed, 12 insertions(+)
 create mode 100644 POP_Mergiar Branchs.md
 rename AlgoritmoDebug.py => Pseudo Python/AlgoritmoDebug.py (100%)
 rename AlgoritmoTipos.py => Pseudo Python/AlgoritmoTipos.py (100%)
 rename AlgoritmosVar.py => Pseudo Python/AlgoritmosVar.py (100%)
 rename Aula02_Procedimentos.py => Pseudo Python/Aula02_Procedimentos.py (100%)
 rename Aula1E_Vetores.py => Pseudo Python/Aula1E_Vetores.py (100%)
 rename Pseu01.py => Pseudo Python/Pseu01.py (100%)


---

thime@ ../Estudos-Python (feat/Updates)
$ git push --set-upstream origin feat/Updates

// resultado 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 621 bytes | 310.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'feat/Updates' on GitHub by visiting:
remote:      https://github.com/Azaton/Estudos-Python/pull/new/feat/Updates
remote:
To github.com:Azaton/Estudos-Python.git
 * [new branch]      feat/Updates -> feat/Updates
branch 'feat/Updates' set up to track 'origin/feat/Updates'.