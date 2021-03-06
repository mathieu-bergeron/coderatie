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

root_dir=$(dirname "$scripts_dir")

script_name=$(basename $(readlink -f $0))

save_dir(){

    current_dir=$(pwd)

}

restore_dir(){

    cd "$current_dir"

}

reminder_message(){
    echo ""
    echo ""
    echo "REMINDER: we publish from github/master"
    echo "REMINDER: changes in ciboulot/mbergeron must be cherry-picked into github/master"
    echo ""
    echo ""
    echo ""
}

auto_commit(){
    git add .
    git commit -a -m"$script_name auto-commit $(date)"
}




