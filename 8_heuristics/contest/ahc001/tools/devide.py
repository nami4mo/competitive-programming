import sys
args=sys.argv
input_filename='out_d.txt'
if len(args)>=2:input_filename=args[1]

# with open('sample.txt', 'w') as f:
#     f.write(text_data)

out_data=[]
chunk=[]
with open(input_filename, 'r') as f:
    data = f.readlines()
    for row in data:
        data=row.rstrip()
        if len(data)<=4:
            # print('a')
            if chunk:
                out_data.append(chunk)
                chunk=[]
        else:
            chunk.append(data)

out_filename_stem=input_filename.split('.')[0]
out_filename_stem=out_filename_stem.split('/')[-1]
for i in range(len(out_data)):
    with open(f'./devided_outs/{out_filename_stem}_{i}.txt','w') as f:
        f.write('\n'.join(out_data[i]))
        f.write('\n')