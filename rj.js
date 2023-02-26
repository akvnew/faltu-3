# https://techwelkin.com/tools/devlys-unicode-devlys-font-converter/#
# --- Read data as string
with open('data.txt', encoding='utf-8') as _:
    data = _.read()
print(data)
# --- Run script now in browser console
data="<paste-here-data-from-above>"
data.split(/\s*[0-9]+\.\s*/).filter(_=>_).map((_, sr)=>(sr+1)+". "+_.split(/\s*\([abcd]\)\s*/).map((__, index)=>{$("#legacy_text").val(__.trim()); convert_to_unicode(); idx=""; if(index>0) {idx = "(" + String.fromCharCode(96+index) + ") "}  return idx+$("#unicode_text").val()}).join(" ")).map(_=>_.replace(" (a)", "\n(a)")).join("\n")

# https://rajasthangyan.com/question?tid=106&start=0&sort=n
del="@"
qs=$$('.maincontent p').map(_=>_.querySelector("span")).filter(_=>_).map(_=>_.innerText.replace(/\s+/g, " ").split(" ").slice(2).join(" ").trim())
opt=$$('.maincontent p').map(_=>Array.from(_.querySelectorAll("span")).slice(1,5)).filter(_=>_.length).map(_=>_.map(__=>__.innerText.split(")").slice(1).join(")").trim()))
ans=$$('.maincontent p').map(_=>_.querySelector("button")).filter(_=>_).map(_=>_.getAttribute('onClick').split("this.innerHTML=")[1].split("").slice(1,-1).join(""))
ans=ans.map((_,idx)=>String.fromCharCode(opt[idx].findIndex(__=>__==_)+65))
ans.map((_,idx)=>[qs[idx], opt[idx].join(del), _].join(del)).join("\n")


# https://www.sawaal.com/general-knowledge/english-questions-and-answers.htm?page=5&sort=
del="@"
qna=$$('.post').map(_=>_.querySelector('.question_and_options_space5')).filter(_=>_).map(_=>_.innerText.replaceAll("\n", " "))
ans=$$('.post').map(_=>_.querySelectorAll('.ansDivBox')).filter(_=>_.length).map(_=>Array.from(_)[1].innerText.split(") ")[0].split(": ")[1])
$$('.post').map(_=>_.querySelectorAll('td')).filter(_=>_.length).map((_,idx)=>[qna[idx],Array.from(_).slice(4).map(_=>_.innerText.replaceAll("\n"," ").trim().split(") ")[1]).join(del),ans[idx]].join(del)).join("\n")

# https://gk-hindi.in/biology-gk
del="@"
qna=$$(".question").map(_=>[_.querySelector("p b").innerText.split(". ").slice(1).join(". "), Array.from(_.querySelectorAll("ul li")).map(_=>_.innerText.split(") ").slice(1).join(") ")).join(del)].join(del))
$$(".question button").map((_,idx)=>[qna[idx], _.getAttribute("data-answer").toUpperCase()].join(del)).join("\n")


# http://www.treeknox.com/bankexams/computer-knowledge/model-4/index.php
del="@"
qna=$$('table.tech').map(_=>[_.querySelector('.th_1').innerText, Array.from(_.querySelectorAll('b')).map(__=>__.innerText).join(del)].join(del))
$$(".view_ans a").map((_,idx)=>[qna[idx],_.getAttributeNode('onclick').nodeValue.split("(")[1].split(")")[0].replace(/[^a-zA-Z]+/g, '').toUpperCase()].join(del)).join("\n")
