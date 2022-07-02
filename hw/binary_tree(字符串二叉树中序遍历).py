import sys
"""
题目：给定二叉树字符串，按照中序遍历顺序为：左子、根、石子数
输入描述：由大小写字母、左右大括号、逗号组成的字符串
1、字母代表一个节点值，左右括号内包含该节点的子节点
2、左右子节点使用逗号分隔，逗号前为空则表示左子节点为空、没有逗号则表示右子节点为空。
3、二叉树节点数最大不超过100。
注：输入字符串格式是正确的，无需考虑格式精误的清况。

输入：a{b{d,e{g,h{,i}}},c{f}}
输出：dbgehiafc
"""


def build(s):
    n, _ = build_node(s[1:])
    n['v'] = s[0]
    return n


def build_node(s, cursor=0):
    start = True
    is_left = True

    lv = ''
    ln = {}

    rv = ''
    rn = {}

    while cursor < len(s):
        c = s[cursor]
        if c == '{':
            if start:
                cursor += 1
                start = False
                continue

            child, cursor = build_node(s, cursor)
            if is_left:
                ln = child
            else:
                rn = child
        elif c == ',':
            is_left = False
            cursor += 1
        elif c == '}':
            cursor += 1
            break
        else:
            if is_left:
                lv = c
            else:
                rv = c
            cursor += 1

    n = {}
    if ln:
        n['l'] = ln
    if lv:
        if 'l' not in n:
            n['l'] = {}
        n['l']['v'] = lv
    if rn:
        n['r'] = rn
    if rv:
        if 'r' not in n:
            n['r'] = {}
        n['r']['v'] = rv
    return n, cursor


def mid_walk(node):
    if 'l' in node:
        mid_walk(node['l'])
    sys.stdout.write(node['v'])
    if 'r' in node:
        mid_walk(node['r'])


root = build(sys.stdin.readline())
mid_walk(root)