import termcolor
#PEGAR EX 3


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs_col((seq_list1), 'blue')


print()
termcolor.cprint("List 2:", 'green')
print_seqs_col(seq_list2, 'green')
