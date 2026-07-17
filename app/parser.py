
import hashlib

def parse_markdown(text):
    nodes=[]
    stack=[]

    lines=text.splitlines()
    current=None

    for line in lines:
        if line.startswith('#'):
            level=line.count('#')
            heading=line.replace('#','').strip()

            parent = stack[level-2]["id"] if level>1 and len(stack)>=level-1 else None

            node={
                "id":len(nodes)+1,
                "heading":heading,
                "body":"",
                "level":level,
                "parent_id":parent,
            }

            while len(stack)>=level:
                stack.pop()

            stack.append(node)
            nodes.append(node)
            current=node

        elif current:
            current["body"] += line+"\n"

    for n in nodes:
        n["content_hash"]=hashlib.sha256(
            n["body"].encode()
        ).hexdigest()

        n["logical_id"]=f'{n["parent_id"]}/{n["heading"]}'

    return nodes
