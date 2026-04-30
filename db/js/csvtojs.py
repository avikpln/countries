'''The csvtojs module'''

import os
import csv

def convert(src, dst=None):
	if not isinstance(src, str):
		raise TypeError('source is not a valid file name')
	if dst and not isinstance(dst, str):
		raise TypeError('destination is not a valid file name')

	dir, filename = os.path.split(src)
	parts = filename.split('.')
	basename, extension = ".".join(parts[:-1]), parts[-1]
	if extension != 'csv':
		raise ValueError('input file should be a CSV file')
	if not dst:
		dst = os.path.join(dir, basename + '.js')
	table_name = basename.upper()

	with open(src, 'r', encoding='utf-8') as incsvfp:
		reader = csv.reader(incsvfp)
		input_rows = [row for row in reader if len(row) > 0]

	# output script
	with open(dst, 'w', encoding='utf-8') as outfp:
		outfp.write(f'const {table_name} = [\n')
		for row in input_rows:
			outfp.write('\t[')
			for i in range(len(row)):
				after = ',' if i < len(row)-1 else '],\n'
				outfp.write(f'"{row[i]}"{after}')
		outfp.write('];\n');
		outfp.write(f'\nexport default {table_name};\n');

def main():
	convert('countries.csv')

if __name__ == '__main__': main()
