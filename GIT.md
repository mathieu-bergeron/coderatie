# `github/master` Vs `ciboulot/mbergeron`

1. `github/master` is the official, published version
1. `ciboulot/mbergeron` is only for me (Mathieu Bergeron)
1. We merge from `github/master` into `ciboulot/mbergeron`
    
        $ git checkout mbergeron
        $ git merge master


1. We cherry-pick or checkout from `ciboulot/mbergeron` to `github/master`

        $ git checkout master
        $ git cherry-pick mbergeron                    # to import a new post that's just been committed

        $ git checkout master
        $ git checkout mbergeron content/fr/test.md    # to import a new file



