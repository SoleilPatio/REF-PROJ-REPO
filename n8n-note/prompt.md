我想要使用n8n做一個每天定時掃描股票市場，將股票走勢傳給LLM，讓LLM幫忙分析作出comment。
請一步一步教我怎麽打造這個專案


curl "https://quickchart.io/chart?c={type:'line',data:{labels:['Mon','Tue','Wed','Thu','Fri'],datasets:[{label:'Price',data:[120,125,130,128,135]}]}}"

curl "https://quickchart.io/chart?c={type:'line',data:{labels:['Mon','Tue','Wed','Thu','Fri'],datasets:[{label:'Price',data:[120,125,130,128,135]}]}}" -o chart.png
start .\chart.png

https://quickchart.io/chart?c={type:'line',data:{labels:['09:00','09:05'],datasets:[{data:[120,121]}]}}