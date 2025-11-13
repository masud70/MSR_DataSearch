keyword_rules_old = [
    '.*energy consum.*', '.*energy efficien.*', '.*energy sav.*', '.*save energy.*', '.*power consum.*', '.*power efficien.*', '.*power sav.*', '.*save power.*',
    [
        ['energy', 'power', 'battery', 'joule'],
        ['sav.*', 'optimi[s|z].*', 'effieien.*', 'consum.*', 'profil.*', 'leak.*', 'drain.*']
    ]
]

keyword_rules_1 = [
    # r"\benergy\s+consum\w*\b",        # "energy consumption", "energy consuming", "energy consumer"
    # r"\bconsum\w*s+energy\b",
    # r"\benergy\s+efficien\w*\b",      # "energy efficient", "energy efficiency"
    # r"\befficien\w*s+energy\b",
    # r"\benergy\s+sav\w*\b",           # "energy saving", "energy saver", "energy savings"
    # r"\bsav\w*\s+energy\b",           # "save energy", "save energy now"

    # r"\bpower\s+consum\w*\b",         # "power consumption", "power consuming"
    # r"\bconsum\w*s+power\b",
    # r"\bpower\s+efficien\w*\b",       # "power efficient", "power efficiency"
    # r"\befficien\w*s+power\b",
    # r"\bpower\s+sav\w*\b",            # "power saving", "power saver", "power savings"
    # r"\bsav\w*\s+power\b",              # "save power"
    
    # Battery specific patterns
    r"\bbattery.*tim",
    r"tim.*battery\b",
    r"\bbattery\b.*\bsav\w*\b",
    r"\bsav\w*\b.*\bbattery\b",
    r"\bbattery\b.*\boptimi[s|z]\w*\b",
    r"\boptimi[s|z]\w*\b.*\bbattery\b",
    r"\bbattery\b.*\befficien\w*\b",
    r"\befficien\w*\b.*\bbattery\b",
    r"\bbattery\b.*\bconsum\w*\b",
    r"\bconsum\w*\b.*\bbattery\b",
    r"\bbattery\b.*\bprofil\w*\b",
    r"\bprofil\w*\b.*\bbattery\b",
    r"\bbattery\b.*\bleak\w*\b",
    r"\bleak\w*\b.*\bbattery\b",
    r"\bbattery\b.*\bdrain\w*\b",
    r"\bdrain\w*\b.*\bbattery\b",
    
    # Energy specific patterns
    r"\benergy\b.*\bsav\w*\b",
    r"\bsav\w*\b.*\benergy\b",
    r"\benergy\b.*\boptimi[s|z]\w*\b", 
    r"\boptimi[s|z]\w*\b.*\benergy\b",
    r"\benergy\b.*\befficien\w*\b",
    r"\befficien\w*\b.*\benergy\b",
    r"\benergy\b.*\bconsum\w*\b",
    r"\bconsum\w*\b.*\benergy\b",
    r"\benergy\b.*\bprofil\w*\b",
    r"\bprofil\w*\b.*\benergy\b",
    r"\benergy\b.*\bleak\w*\b",
    r"\bleak\w*\b.*\benergy\b",
    r"\benergy\b.*\bdrain\w*\b",
    r"\bdrain\w*\b.*\benergy\b",
    
    # Power specific patterns
    r"\bpower\b.*\bsav\w*\b",
    r"\bsav\w*\b.*\bpower\b",
    r"\bpower\b.*\boptimi[s|z]\w*\b",
    r"\boptimi[s|z]\w*\b.*\bpower\b",
    r"\bpower\b.*\befficien\w*\b",
    r"\befficien\w*\b.*\bpower\b",
    r"\bpower\b.*\bconsum\w*\b",
    r"\bconsum\w*\b.*\bpower\b",
    r"\bpower\b.*\bprofil\w*\b",
    r"\bprofil\w*\b.*\bpower\b",
    r"\bpower\b.*\bleak\w*\b",
    r"\bleak\w*\b.*\bpower\b",
    r"\bpower\b.*\bdrain\w*\b",
    r"\bdrain\w*\b.*\bpower\b"
    
    # [
    #     [
    #         r"\benergy\b",
    #         r"\bpower\b",
    #         r"\bbattery\b",
    #     ],
    #     [
    #         r"\bsav\w*\b",           # save, saving, savings, saver
    #         r"\boptimi[s|z]\w*\b",   # optimize/optimise/optimized/optimisation...
    #         r"\befficien\w*\b",      # efficient, efficiency
    #         r"\bconsum\w*\b",        # consume, consuming, consumption
    #         r"\bprofil\w*\b",        # profile, profiling, profiler
    #         r"\bleak\w*\b",          # leak, leaking, leakage
    #         r"\bdrain\w*\b",         # drain, draining, battery drain, power drain
    #     ],
    # ]
]

keyword_rules = [
    # Battery specific patterns
    r"\bbattery.*tim",
    r"tim.*battery\b",
    r"\bbattery.*sav\w*\b",
    r"\bsav.*battery\b",
    r"\bbattery.*optimi[s|z]\w*\b",
    r"\boptimi[s|z].*battery\b",
    r"\bbattery.*efficien\w*\b",
    r"\befficien.*battery\b",
    r"\bbattery.*consum\w*\b",
    r"\bconsum.*battery\b",
    r"\bbattery.*profil\w*\b",
    r"\bprofil.*battery\b",
    r"\bbattery.*leak\w*\b",
    r"\bleak.*battery\b",
    r"\bbattery.*drain\w*\b",
    r"\bdrain.*battery\b",
    
    # Energy specific patterns
    r"\benergy.*sav\w*\b",
    r"\bsav.*energy\b",
    r"\benergy.*optimi[s|z]\w*\b", 
    r"\boptimi[s|z].*energy\b",
    r"\benergy.*efficien\w*\b",
    r"\befficien.*energy\b",
    r"\benergy.*consum\w*\b",
    r"\bconsum.*energy\b",
    r"\benergy.*profil\w*\b",
    r"\bprofil.*energy\b",
    r"\benergy.*leak\w*\b",
    r"\bleak.*energy\b",
    r"\benergy.*drain\w*\b",
    r"\bdrain.*energy\b",
    
    # Power specific patterns
    r"\bpower.*sav\w*\b",
    r"\bsav.*power\b",
    r"\bpower.*optimi[s|z]\w*\b",
    r"\boptimi[s|z].*power\b",
    r"\bpower.*efficien\w*\b",
    r"\befficien.*power\b",
    r"\bpower.*consum\w*\b",
    r"\bconsum.*power\b",
    r"\bpower.*profil\w*\b",
    r"\bprofil.*power\b",
    r"\bpower.*leak\w*\b",
    r"\bleak.*power\b",
    r"\bpower.*drain\w*\b",
    r"\bdrain.*power\b"
]

keywords = [
    r'energy.*consum',  r'consum.*energy', r'energy.*efficien',r'efficien.*energy', r'energy.*sav', r'sav.*energy',  r'energy.*optimi[sz]', r'optimi[sz].*energy',
    r'energy.*leak', r'leak.*energy', r'energy.*drain', r'drain.*energy', r'energy.*profil', r'profil.*energy',

    r'power.*consum',  r'consum.*power', r'power.*efficien',r'efficien.*power',  r'power.*sav', r'sav.*power',    r'power.*optimi[sz]', r'optimi[sz].*power',
    r'power.*leak', r'leak.*power', r'power.*drain', r'drain.*power',r'power.*profil', r'profil.*power',

    r'battery.*consum',  r'consum.*battery', r'battery.*efficien',r'efficien.*battery', r'battery.*sav', r'sav.*battery',  r'battery.*optimi[sz]', r'optimi[sz].*battery',
    r'battery.*leak', r'leak.*battery', r'battery.*drain', r'drain.*battery', r'battery.*tim', r'tim.*battery',r'battery.*profil', r'profil.*battery',
    # [[],[]]
]

keywords2 = [
    r'energy.*consum',  r'consum.*energy', r'energy.*efficien',r'efficien.*energy', r'energy.*sav', r'sav.*energy',  r'energy.*optimi[sz]', r'optimi[sz].*energy',
    r'energy.*leak', r'leak.*energy', r'energy.*drain', r'drain.*energy', r'energy.*profil', r'profil.*energy', r'energy.*tim', r'tim.*energy',

    r'power.*consum',  r'consum.*power', r'power.*efficien',r'efficien.*power',  r'power.*sav', r'sav.*power',    r'power.*optimi[sz]', r'optimi[sz].*power',
    r'power.*leak', r'leak.*power', r'power.*drain', r'drain.*power',r'power.*profil', r'profil.*power', r'power.*tim', r'tim.*power',

    r'battery.*consum',  r'consum.*battery', r'battery.*efficien',r'efficien.*battery', r'battery.*sav', r'sav.*battery',  r'battery.*optimi[sz]', r'optimi[sz].*battery',
    r'battery.*leak', r'leak.*battery', r'battery.*drain', r'drain.*battery', r'battery.*tim', r'tim.*battery', r'battery.*profil', r'profil.*battery', 
    
    # New added
    r'energy.*track', r'track.*energy', r'energy.*monitor', r'monitor.*energy', r'energy.*manag', r'manag.*energy', r'energy.*calculat', r'calculat.*energy', r'energy.*comput', r'comput.*energy',
    r'power.*track', r'track.*power', r'power.*monitor', r'monitor.*power', r'power.*manag', r'manag.*power', r'power.*calculat', r'calculat.*power', r'power.*comput', r'comput.*power',
    r'battery.*track', r'track.*battery', r'battery.*monitor', r'monitor.*battery', r'battery.*manag', r'manag.*battery', r'battery.*calculat', r'calculat.*battery', r'battery.*comput', r'comput.*battery',
]

keywords_v1 = [
    r'(energy|power|battery).*(consum|efficien|sav|optimi[sz]|leak|drain|profil|tim)',
    r'(consum|efficien|sav|optimi[sz]|leak|drain|profil|tim).*(energy|power|battery)',
    
    # r'(battery).*(tim)',
    # r'(tim).*(battery)',
]

keywords_v2 = [
    r'(energy|power|battery).*(consum|efficien|sav|optimi[sz]|leak|drain|profil|track|monitor|manag|calculat|comput|tim)',
    r'(consum|efficien|sav|optimi[sz]|leak|drain|profil|track|monitor|manag|calculat|comput|tim).*(energy|power|battery)',
]