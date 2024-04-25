# please export all stocks as a list for other python modules to use
# Approximately 300 stocks here

all_stocks = ['MSFT', 'VEEV', 'NVDA', 'AMZN', 'META', 'GOOGL', 'GOOG', 'SSD', 'LLY', 'AVGO', 'JPM', 'XOM', 'TSLA', 'V', 'UNH', 'MA', 'PG', 'JNJ', 'HD', 'COST', 'MRK', 'ABBV', 'CRM', 'CVX', 'NFLX', 'AMD', 'WMT', 'BAC', 'PEP', 'KO', 'TMO', 'LIN', 'ADBE', 'DIS', 'WFC', 'ACN', 'CSCO', 'MCD', 'ORCL', 'QCOM', 'ABT', 'CAT', 'INTU', 'AMAT', 'GE', 'VZ', 'IBM', 'DHR', 'NOW', 'CMCSA', 'UBER', 'COP', 'TXN', 'INTC', 'PFE', 'AMGN', 'UNP', 'PM', 'ISRG', 'MU', 'SPGI', 'LOW', 'RTX', 'NEE', 'HON', 'ETN', 'GS', 'LRCX', 'AXP', 'BKNG', 'PGR', 'ELV', 'T', 'SYK', 'C', 'NKE', 'PLD', 'MS', 'TJX', 'BLK', 'MDT', 'UPS', 'SCHW', 'DE', 'CI', 'VRTX', 'ADP', 'BSX', 'CB', 'BMY', 'MMC', 'BA', 'LMT', 'SBUX', 'ADI', 'REGN', 'KLAC', 'FI', 'MDLZ', 'BX', 'PANW', 'CVS', 'GILD', 'SNPS', 'TMUS', 'AMT', 'CDNS', 'CMG', 'EOG', 'MPC', 'TGT', 'ICE', 'CME', 'WM', 'SO', 'SHW', 'SLB', 'DUK', 'MO', 'EQIX', 'FCX', 'PH', 'CL', 'PSX', 'CSX', 'PYPL', 'ITW', 'ABNB', 'ZTS', 'MCK', 'BDX', 'ANET', 'TT', 'APH', 'TDG', 'GD', 'USB', 'NOC', 'EMR', 'HCA', 'ORLY', 'PXD', 'MAR', 'FDX', 'PCAR', 'AON', 'CEG', 'NXPI', 'PNC', 'MCO', 'VLO', 'CTAS', 'MSI', 'ROP', 'ECL', 'NSC', 'EW', 'COF', 'DXCM', 'HLT', 'AIG', 'APD', 'AZO', 'ADSK', 'AJG', 'TRV', 'MMM', 'GM', 'WELL', 'F', 'TFC', 'CPRT', 'NUE', 'CARR', 'SPG', 'WMB', 'MCHP', 'ROST', 'OKE', 'URI', 'DHI', 'OXY', 'SMCI', 'NEM', 'JCI', 'TEL', 'ALL', 'SRE', 'O', 'DLR', 'AEP', 'PSA', 'MET', 'IQV', 'AFL', 'GWW', 'STZ', 'HES', 'FTNT', 'FIS', 'CCI', 'KMB', 'AMP', 'BK', 'MSCI', 'AME', 'IDXX', 'A', 'D', 'ROK', 'CDW', 'ADM', 'DG', 'VRSK', 'EL', 'GPN', 'DD', 'PPG', 'MPWR', 'KDP', 'EA', 'XYL', 'ED', 'EFX', 'DFS', 'DAL', 'RCL', 'EXR', 'HIG', 'XEL', 'FICO', 'ANSS', 'FTV', 'VICI', 'BIIB', 'ON', 'KHC', 'WST', 'HSY', 'KEYS', 'MTD', 'RMD', 'WTW', 'EBAY', 'CBRE', 'TSCO', 'EIX', 'WAB', 'DLTR', 'ZBH', 'CAH', 'LYB', 'AVB', 'CHTR', 'TROW', 'TRGP', 'HWM', 'WEC', 'NVR', 'HPQ', 'CHD', 'WY', 'DOV', 'GLW', 'PHM', 'FITB', 'BR', 'NDAQ', 'BLDR', 'STT', 'TTWO', 'WDC', 'RJF', 'AWK', 'ALGN', 'HPE', 'MTB', 'IRM', 'AXON', 'GRMN', 'DTE', 'SMCI', 'DOC', 'AMCR', 'IP', 'WBA', 'RVTY', 'ROL', 'TAP', 'CRL', 'PODD', 'JKHY', 'WRK', 'LNT', 'KIM', 'GEN', 'EVRG', 'IPG', 'JNPR', 'EMN', 'MGM', 'LW', 'KMX', 'AES', 'SJM', 'ALLE', 'FFIV', 'UDR', 'HII', 'NI', 'QRVO', 'AOS', 'TECH', 'CPT', 'APA', 'BBWI', 'CTLT', 'UHS', 'MOS', 'TFX', 'INCY', 'HRL', 'WYNN', 'PAYC', 'REG', 'TPR', 'NWSA', 'DAY', 'HSIC', 'AIZ', 'BF.B', 'MTCH', 'SOLV', 'AAL', 'BXP', 'CZR', 'CPB', 'CHRW', 'PNW', 'GNRC', 'ETSY', 'MKTX', 'BWA', 'RHI', 'FOXA', 'NCLH', 'FRT', 'BEN', 'FMC', 'HAS', 'DVA', 'IVZ', 'CMA', 'RL', 'BIO', 'MHK', 'PARA', 'GL', 'FOX', 'NWS']
##RUSSELL 1000 - top 1000 stocks by Market Cap - commented out does not have data available for whatever reason
all_stocks2 = ["A", "AA", "AAL", "AAP", "AAPL", "ABBV", "ABNB", "ABT", "ACGL", "ACHC", "ACI", "ACM", "ACN", "ADBE", "ADC", "ADI", "ADM", "ADP", "ADSK", "ADT", "AEE", "AEP", "AES", "AFG", "AFL", "AFRM", "AGCO", "AGL", "AGNC", "AGO", "AGR", "AIG", "AIRC", "AIZ", "AJG", "AKAM", "AL", "ALB", "ALGM", "ALGN", "ALK", "ALL", "ALLE", "ALLY", "ALNY", "ALSN", "AM", "AMAT", "AMBP", "AMC", "AMCR", "AMD", "AME", "AMED", "AMG", "AMGN", "AMH", "AMP", "AMT", "AMZN", "AN", "ANET", "ANSS", "AON", "AOS", "APA", "APD", "APH", "APLS", "APO", "APP", "APTV", "AR", "ARE", "ARES", "ARMK", "ARW", "ASH", "ATO", "ATR", "AVB", "AVGO", "AVT", "AVTR", "AVY", "AWI", "AWK", "AXON", "AXP", "AXS", "AXTA", "AYI", "AZEK", "AZO", "AZPN", "AZTA", "BA", "BAC", "BAH", "BALL", "BAX", "BBWI", "BBY", "BC", "BDX", "BEN", "BEPC", "BERY", "BF.A", "BFAM", "BF.B", "BG", "BHF", "BIIB", "BILL", "BIO", 
              #"BIRK", 
              "BJ", "BK", "BKNG", "BKR", "BLD", "BLDR", "BLK", "BMRN", "BMY", "BOKF", "BPOP", "BR", "BRK.B", "BRKR", "BRO", "BRX", "BSX", "BSY", "BURL", "BWA", "BWXT", "BX", "BXP", "BYD", "C", "CABO", "CACC", "CACI", "CAG", "CAH", "CAR", "CARR", "CART", "CASY", "CAT", "CAVA", "CB", "CBOE", "CBRE", "CBSH", "CC", "CCCS", "CCI", "CCK", "CCL", "CDNS", "CDW", "CE", "CEG", "CELH", "CERT", "CF", "CFG", "CFLT", "CFR", "CG", "CGNX", "CHD", "CHDN", "CHE", "CHH", "CHK", "CHPT", "CHRW", "CHTR", "CI", "CIEN", "CINF", "CL", "CLF", "CLH", "CLVT", "CLX", "CMA", "CMCSA", "CME", "CMG", "CMI", "CMS", "CNA", "CNC", "CNHI", "CNM", "CNP", "CNXC", "COF", "COHR", "COIN", "COLB", "COLD", "COLM", "COO", "COP", "COR", "COST", "COTY", 
              #"CPAY", 
              "CPB", "CPNG", "CPRI", "CPRT", "CPT", "CR", "CRI", "CRL", "CRM", "CROX", "CRUS", "CRWD", "CSCO", "CSGP", "CSL", "CSX", "CTAS", "CTLT", "CTRA", "CTSH", "CTVA", "CUBE", "CUZ", "CVS", "CVX", "CW", "CWEN", 
              #"CWE.A", 
              "CXT", "CZR", "D", "DAL", "DAR", "DASH", 
              #"DAY", 
              "DBX", "DCI", "DD", "DDOG", "DE", "DECK", "DFS", "DG", "DGX", "DHI", "DHR", "DINO", "DIS", "DKNG", "DKS", "DLB", "DLR", "DLTR", "DNA", "DNB", "DOC", "DOCS", "DOCU", "DOV", "DOW", "DOX", "DPZ", "DRI", "DRVN", "DT", "DTE", "DTM", "DUK", "DV", "DVA", "DVN", "DXC", "DXCM", "EA", "EBAY", "ECL", "ED", "EEFT", "EFX", 
              #"EG", 
              "EGP", "EHC", "EIX", "EL", "ELAN", "ELS", "ELV", "EME", "EMN", "EMR", "ENOV", "ENPH", "ENTG", "EOG", "EPAM", "EPR", "EQH", "EQIX", "EQR", "EQT", "ES", "ESAB", "ESI", "ESS", "ESTC", "ETN", "ETR", "ETSY", "EVR", "EVRG", "EW", "EWBC", "EXAS", "EXC", "EXEL", "EXP", "EXPD", "EXPE", "EXR", "F", "FAF", "FANG", "FAST", "FBIN", "FCN", "FCNCA", "FCX", "FDS", "FDX", "FE", "FERG", "FFIV", "FHB", "FHN", "FI", "FICO", "FIS", "FITB", "FIVE", "FIVN", "FLO", "FLS", "FMC", "FNB", "FND", "FNF", "FOUR", "FOX", "FOXA", "FR", "FRPT", "FRT", "FSLR", "FTI", "FTNT", "FTRE", "FTV", "FWONA", "FWONK", "FYBR", "G", "GD", "GDDY", "GE", "GEHC", "GEN", "GFS", "GGG", "GILD", "GIS", "GL", "GLOB", "GLPI", "GLW", "GM", "GME", "GMED", "GNRC", "GNTX", "GO", "GOOG", "GOOGL", "GPC", "GPK", "GPN", "GPS", "GRMN", "GS", "GTES", "GTLB", "GWRE", "GWW", "GXO", "H", "HAL", "HAS", "HAYW", "HBAN", "HCA", "HCP", "HD", "HE", "HEI", "HEI.A", "HES", 
              #"HHH", 
              "HIG", "HII", "HIW", "HLI", "HLT", "HOG", "HOLX", "HON", "HOOD", "HPE", "HPQ", "HR", "HRB", "HRL", "HSIC", "HST", "HSY", "HTZ", "HUBB", "HUBS", "HUM", "HUN", "HWM", "HXL", "IAC", "IART", "IBKR", "IBM", "ICE", "ICLR", "ICUI", "IDA", "IDXX", "IEX", "IFF", "ILMN", "INCY", "INFA", "INGR", "INSP", "INTC", "INTU", "INVH", "IONS", "IP", "IPG", "IPGP", "IQV", "IR", "IRDM", "IRM", "ISRG", "IT", "ITT", "ITW", "IVZ", "J", "JAZZ", "JBHT", "JBL", "JCI", "JEF", "JHG", "JKHY", "JLL", "JNJ", "JNPR", "JPM", "JWN", "K", "KBR", "KD", "KDP", "KEX", "KEY", "KEYS", "KHC", "KIM", "KKR", "KLAC", "KLG", "KMB", "KMI", "KMPR", "KMX", "KNSL", "KNX", "KO", "KR", "KRC", "KSS", "KVUE", "L", "LAD", "LAMR", "LAZ", "LBRDA", "LBRDK", "LCID", "LDOS", "LEA", "LECO", "LEG", "LEN", "LEN.B", "LFUS", "LH", "LHX", "LII", "LIN", "LITE", "LKQ", "LLY", 
              #"LLYVA", 
              #"LLYVK", 
              "LMT", "LNC", "LNG", "LNT", "LOPE", "LOW", "LPLA", "LPX", "LRCX", "LSCC", "LSTR", "LSXMA", "LSXMK", "LULU", "LUV", "LVS", "LW", "LYB", "LYFT", "LYV", "M", "MA", "MAA", "MAN", "MANH", "MAR", "MAS", "MASI", "MAT", "MCD", "MCHP", "MCK", "MCO", "MCW", "MDB", "MDLZ", "MDT", "MDU", "MEDP", "MET", "META", "MGM", "MHK", "MIDD", "MKC", "MKL", "MKSI", "MKTX", "MLM", "MMC", "MMM", "MNST", "MO", "MOH", "MORN", "MOS", "MP", "MPC", "MPW", "MPWR", "MRCY", "MRK", "MRNA", "MRO", "MRVI", "MRVL", "MS", "MSA", "MSCI", "MSFT", "MSGS", "MSI", "MSM", "MTB", "MTCH", "MTD", "MTG", "MTN", "MTZ", "MU", "MUSA", "NATL", "NBIX", "NCLH", "NCNO", "NDAQ", "NDSN", "NEE", "NEM", "NET", "NEU", "NFE", "NFG", "NFLX", "NI", "NKE", 
              #"NLOP", 
              "NLY", "NNN", "NOC", "NOV", "NOW", "NRG", "NSA", "NSC", "NTAP", "NTNX", "NTRA", "NTRS", "NU", "NUE", "NVCR", "NVDA", "NVR", "NVST", "NVT", "NWL", "NWS", "NWSA", "NXST", "NYCB", "NYT", "O", "OC", "ODFL", "OGE", "OGN", "OHI", "OKE", "OKTA", "OLED", "OLLI", "OLN", "OLPX", "OMC", "OMF", "ON", "ORCL", "ORI", "ORLY", "OSK", "OTIS", "OVV", "OWL", "OXY", "OZK", "PAG", "PANW", "PARA", 
              #"PARAA", 
              "PATH", "PAYC", "PAYX", "PB", "PCAR", "PCG", "PCOR", "PCTY", "PEG", "PEGA", "PEN", "PENN", "PEP", "PFE", "PFG", "PFGC", "PG", "PGR", "PH", 
              #"PHIN", 
              "PHM", "PII", "PINC", "PINS", "PK", "PKG", "PLD", "PLNT", "PLTK", "PLTR", "PLUG", "PM", "PNC", "PNFP", "PNR", "PNW", "PODD", "POOL", "POST", "PPC", "PPG", "PPL", "PRGO", "PRI", "PRU", "PSA", "PSTG", "PSX", "PTC", "PTON", "PVH", "PWR", "PXD", "PYCR", "PYPL", "QCOM", "QDEL", "QGEN", "QRVO", "QS", "R", "RARE", "RBA", "RBC", "RBLX", "RCL", "RCM", "REG", "REGN", "REXR", "REYN", "RF", "RGA", "RGEN", "RGLD", "RH", "RHI", 
              #"RITM", 
              "RIVN", "RJF", "RKT", "RL", "RLI", "RMD", "RNG", "RNR", "ROIV", "ROK", "ROKU", "ROL", "ROP", "ROST", "RPM", "RPRX", "RRC", "RRX", "RS", "RSG", "RTX", "RUN", "RVTY", "RYAN", "RYN", "S", "SAIA", "SAIC", "SAM", "SBAC", "SBUX", "SCCO", "SCHW", "SCI", "SEB", "SEE", "SEIC", "SF", "SHC", "SHW", "SIRI", "SITE", "SJM", "SKX", "SLB", "SLGN", "SLM", "SMAR", "SMG", "SNA", "SNDR", "SNOW", "SNPS", "SNV", "SNX", "SO", "SOFI", "SON", "SPB", "SPG", "SPGI", "SPOT", "SPR", "SQ", "SRCL", "SRE", "SRPT", "SSNC", "SSRM", "ST", "STAG", "STE", "STLD", "STT", "STWD", "STZ", "SUI", "SWAV", "SWK", "SWKS", "SWN", "SYF", "SYK", "SYY", "T", "TAP", "TDC", "TDG", "TDOC", "TDY", "TEAM", "TECH", "TER", "TFC", "TFSL", "TFX", "TGT", "THC", "THG", "THO", "TJX", "TKO", "TKR", "TMO", "TMUS", "TNDM", "TNL", "TOL", "TOST", "TPG", "TPL", "TPR", "TPX", "TREX", "TRGP", "TRIP", "TRMB", "TROW", "TRU", "TRV", "TSCO", "TSLA", "TSN", "TT", "TTC", "TTD", "TTEK", "TTWO", "TW", "TWLO", "TXG", "TXN", "TXRH", "TXT", "TYL", "U", "UA", "UAA", "UAL", "UBER", "UDR", "UGI", "UHAL", 
              #"UHA.B", 
              "UHS", "UI", "ULTA", "UNH", "UNM", "UNP", "UPS", "URI", "USB", "USFD", "UTHR", "UWMC", "V", "VAC", "VEEV", "VFC", "VICI", "VIRT", "VLO", 
              #"VLTO", 
              "VMC", "VMI", "VNO", "VNT", "VOYA", "VRSK", "VRSN", "VRT", "VRTX", "VSAT", "VSCO", "VST", 
              #"VSTS", 
              "VTR", "VTRS", "VVV", "VYX", "VZ", "W", "WAB", "WAL", "WAT", "WBA", "WBD", "WBS", "WCC", "WDAY", "WDC", "WEC", "WELL", "WEN", "WEX", "WFC", "WH", "WHR", "WING", "WLK", "WM", "WMB", "WMS", "WMT", "WOLF", "WOOF", "WPC", "WRB", "WRK", "WSC", "WSM", "WSO", "WST", "WTFC", "WTM", "WTRG", "WTW", "WU", "WWD", "WY", "WYNN", "X", "XEL", "XOM", "XP", "XPO", "XRAY", "XYL", "YETI", "YUM", "Z", "ZBH", "ZBRA", "ZG", "ZI", "ZION" ]



