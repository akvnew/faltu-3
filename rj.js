# https://gk-hindi.in/biology-gk
del="@"
qna=$$(".question").map(_=>[_.querySelector("p b").innerText.split(". ").slice(1).join(". "), Array.from(_.querySelectorAll("ul li")).map(_=>_.innerText.split(") ").slice(1).join(") ")).join(del)].join(del))
$$(".question button").map((_,idx)=>[qna[idx], _.getAttribute("data-answer").toUpperCase()].join(del)).join("\n")


# http://www.treeknox.com/bankexams/computer-knowledge/model-4/index.php
del="@"
qna=$$('table.tech').map(_=>[_.querySelector('.th_1').innerText, Array.from(_.querySelectorAll('b')).map(__=>__.innerText).join(del)].join(del))
$$(".view_ans a").map((_,idx)=>[qna[idx],_.getAttributeNode('onclick').nodeValue.split("(")[1].split(")")[0].replace(/[^a-zA-Z]+/g, '').toUpperCase()].join(del)).join("\n")
