# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vparekh <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 13:00:44 by vparekh           #+#    #+#              #
#    Updated: 2019/11/04 14:23:24 by vparekh          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args_len = len(sys.argv)
i = 1
ostr = ""
while (i < args_len):
    ostr += str(sys.argv[i])
    if (i + 1 < args_len):
        ostr += " "
    i += 1
ostr = ostr[::-1]
print(ostr.swapcase())


