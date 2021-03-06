# Copyright (C) (2019) (Mathieu Bergeron) (mathieu.bergeron@cmontmorency.qc.ca)
#
# This file is part of tp01_menu
#
# aquiletour is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# aquiletour is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with aquiletour.  If not, see <https://www.gnu.org/licenses/>

##### INCLUDE #####
this_dir=$(readlink -f $0)
scripts_dir=$(dirname "$this_dir")
. "$scripts_dir/include.sh"
###################

save_dir

cd "$root_dir"

reminder_message(){
    echo ""
    echo ""
    echo "REMINDER: we publish from github/master"
    echo "REMINDER: changes in ciboulot/mbergeron must be cherry-picked into github/master"
    echo ""
    echo ""
    echo ""
}

reminder_message

auto_commit
git push

git checkout master
git push

# refresh public
rm -rf public
hugo

# rsync to server
rsync -r --delete public/* coderatie.org:~/perso/coderatie/
rsync -r --delete content/fr/decembre2020 coderatie.org:~/perso/coderatie/fr/

git checkout mbergeron


reminder_message

restore_dir
