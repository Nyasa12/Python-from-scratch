Letter = '''Dear <|Name|>
           You are selected! 
 <|Date|>'''

print(Letter.replace("<|Name|>", "Nyasa").replace("<|Date|>", "\"25th november 2025\""))