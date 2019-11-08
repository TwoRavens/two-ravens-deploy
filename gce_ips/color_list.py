
domain_colors = """
apricot
black
blue
brown
cyan
green
grey
lavender
lime
magneta
maroon
mint
navy
olive
orange
pink
purple
red
white
yellow""".split('\n')

domain_colors = [x.strip().lower()
                 for x in domain_colors
                 if x.strip()]

cnt = 0
for dcolor in domain_colors:
    cnt += 1
    #print(f'\n\n-- {cnt} {dcolor} --')
    stmt = (f'gcloud compute addresses create raven-test-ip-{dcolor}'
            f' --region us-central1')
    print(stmt)
