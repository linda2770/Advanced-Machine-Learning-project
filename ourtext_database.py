good_model_demo_1="\
2018-12-14 22:31:28.016098: step 100, loss = 8.270716 (28.9 examples/sec)\
2018-12-14 22:33:03.998145: step 200, loss = 7.094165 (33.3 examples/sec)\
=> 2018-12-14 22:34:40.217776: step 300, loss = 6.990337 (33.3 examples/sec)\
=> 2018-12-14 22:36:15.820347: step 400, loss = 6.323220 (33.5 examples/sec)\
=> 2018-12-14 22:37:51.196736: step 500, loss = 6.435486 (33.6 examples/sec)\
=> 2018-12-14 22:39:26.811960: step 600, loss = 7.159293 (33.5 examples/sec)\
=> 2018-12-14 22:41:02.088956: step 700, loss = 6.052781 (33.6 examples/sec)\
=> 2018-12-14 22:42:37.961249: step 800, loss = 6.209580 (33.4 examples/sec)\
=> 2018-12-14 22:44:14.092207: step 900, loss = 6.349383 (33.3 examples/sec)\
=> 2018-12-14 22:45:49.767289: step 1000, loss = 5.330081 (33.4 examples/sec)\
=> Evaluating on validation dataset...\
=> 2018-12-14 22:50:27.800091: step 1100, loss = 5.529603 (33.1 examples/sec)\
=> 2018-12-14 22:52:05.204818: step 1200, loss = 5.594587 (32.9 examples/sec)\
=> 2018-12-14 22:53:41.146937: step 1300, loss = 5.000809 (33.4 examples/sec)\
=> 2018-12-14 22:55:17.091904: step 1400, loss = 4.190656 (33.4 examples/sec)\
=> 2018-12-14 22:56:52.773725: step 1500, loss = 4.842415 (33.4 examples/sec)\
=> 2018-12-14 22:58:28.664277: step 1600, loss = 4.189437 (33.4 examples/sec)\
=> 2018-12-14 23:00:04.651703: step 1700, loss = 4.150048 (33.3 examples/sec)\
=> 2018-12-14 23:01:40.443803: step 1800, loss = 4.372252 (33.4 examples/sec)\
=> 2018-12-14 23:03:16.342316: step 1900, loss = 3.211534 (33.4 examples/sec)\
=> 2018-12-14 23:04:52.271666: step 2000, loss = 3.626893 (33.4 examples/sec)\
=> 2018-12-14 23:09:28.671648: step 2100, loss = 2.751443 (33.6 examples/sec)\
=> 2018-12-14 23:11:04.463452: step 2200, loss = 2.972907 (33.4 examples/sec)\
=> 2018-12-14 23:12:40.440430: step 2300, loss = 2.916949 (33.3 examples/sec)\
=> 2018-12-14 23:14:16.060978: step 2400, loss = 2.716969 (33.5 examples/sec)\
=> 2018-12-14 23:15:52.013941: step 2500, loss = 2.196689 (33.4 examples/sec)\
=> 2018-12-14 23:17:27.963218: step 2600, loss = 1.922568 (33.4 examples/sec)\
=> 2018-12-14 23:19:03.754321: step 2700, loss = 2.873019 (33.4 examples/sec)\
=> 2018-12-14 23:20:39.776057: step 2800, loss = 2.645671 (33.3 examples/sec)\
=> 2018-12-14 23:22:15.340269: step 2900, loss = 1.829109 (33.5 examples/sec)\
=> 2018-12-14 23:23:51.145238: step 3000, loss = 1.794580 (33.4 examples/sec)\
=> 2018-12-14 23:28:28.331221: step 3100, loss = 1.701109 (33.3 examples/sec)\
=> 2018-12-14 23:30:04.209214: step 3200, loss = 1.158688 (33.4 examples/sec)\
=> 2018-12-14 23:31:40.303740: step 3300, loss = 1.688568 (33.3 examples/sec)\
=> 2018-12-14 23:33:16.223841: step 3400, loss = 1.181412 (33.4 examples/sec)\
=> 2018-12-14 23:34:52.070517: step 3500, loss = 1.276613 (33.4 examples/sec)\
=> 2018-12-14 23:36:28.234483: step 3600, loss = 1.228202 (33.3 examples/sec)\
=> 2018-12-14 23:38:04.080708: step 3700, loss = 1.130294 (33.4 examples/sec)\
=> 2018-12-14 23:39:39.718890: step 3800, loss = 1.066740 (33.5 examples/sec)\
=> 2018-12-14 23:41:15.939134: step 3900, loss = 1.171784 (33.3 examples/sec)\
=> 2018-12-14 23:42:52.074248: step 4000, loss = 1.427454 (33.3 examples/sec)\
=> 2018-12-14 23:47:31.686118: step 4100, loss = 0.991590 (33.3 examples/sec)\
=> 2018-12-14 23:49:07.607781: step 4200, loss = 1.876052 (33.4 examples/sec)\
=> 2018-12-14 23:50:43.382994: step 4300, loss = 1.051316 (33.4 examples/sec)\
=> 2018-12-14 23:52:19.541156: step 4400, loss = 0.832901 (33.3 examples/sec)\
=> 2018-12-14 23:53:55.471283: step 4500, loss = 1.650633 (33.4 examples/sec)\
=> 2018-12-14 23:55:31.122212: step 4600, loss = 1.090806 (33.5 examples/sec)\
=> 2018-12-14 23:57:07.139553: step 4700, loss = 1.197399 (33.3 examples/sec)\
=> 2018-12-14 23:58:43.114774: step 4800, loss = 1.426502 (33.3 examples/sec)\
=> 2018-12-15 00:00:18.748749: step 4900, loss = 1.541100 (33.5 examples/sec)\
=> 2018-12-15 00:01:54.902240: step 5000, loss = 1.341852 (33.3 examples/sec)\
=> 2018-12-15 00:06:34.606293: step 5100, loss = 0.469521 (33.4 examples/sec)\
=> 2018-12-15 00:08:10.839958: step 5200, loss = 1.724318 (33.3 examples/sec)\
=> 2018-12-15 00:09:46.998319: step 5300, loss = 0.797721 (33.3 examples/sec)\
=> 2018-12-15 00:11:22.884879: step 5400, loss = 0.713887 (33.4 examples/sec)\
=> 2018-12-15 00:12:59.289333: step 5500, loss = 1.175849 (33.2 examples/sec)\
=> 2018-12-15 00:14:35.445040: step 5600, loss = 1.271648 (33.3 examples/sec)\
=> 2018-12-15 00:16:11.590140: step 5700, loss = 1.769381 (33.3 examples/sec)\
=> 2018-12-15 00:17:47.717713: step 5800, loss = 1.148689 (33.3 examples/sec)\
=> 2018-12-15 00:19:23.679379: step 5900, loss = 1.006708 (33.3 examples/sec)\
=> 2018-12-15 00:20:59.725594: step 6000, loss = 0.905720 (33.3 examples/sec)\
=> 2018-12-15 00:25:39.203728: step 6100, loss = 0.732879 (33.4 examples/sec)\
=> 2018-12-15 00:27:15.122908: step 6200, loss = 0.765667 (33.4 examples/sec)\
=> 2018-12-15 00:28:51.451359: step 6300, loss = 0.626755 (33.2 examples/sec)\
=> 2018-12-15 00:30:27.255970: step 6400, loss = 2.364927 (33.4 examples/sec)\
=> 2018-12-15 00:32:03.023341: step 6500, loss = 0.748249 (33.4 examples/sec)\
=> 2018-12-15 00:33:39.410276: step 6600, loss = 1.381666 (33.2 examples/sec)\
=> 2018-12-15 00:35:15.401318: step 6700, loss = 0.885097 (33.3 examples/sec)\
=> 2018-12-15 00:36:51.264811: step 6800, loss = 1.983609 (33.4 examples/sec)\
=> 2018-12-15 00:38:27.531207: step 6900, loss = 1.658035 (33.2 examples/sec)\
=> 2018-12-15 00:40:03.722096: step 7000, loss = 1.081374 (33.3 examples/sec)\
=> 2018-12-15 00:44:40.932176: step 7100, loss = 0.614269 (33.2 examples/sec)\
=> 2018-12-15 00:46:16.741431: step 7200, loss = 2.972046 (33.4 examples/sec)\
=> 2018-12-15 00:47:52.471353: step 7300, loss = 0.559086 (33.4 examples/sec)\
=> 2018-12-15 00:49:28.794087: step 7400, loss = 0.937687 (33.2 examples/sec)\
=> 2018-12-15 00:51:04.638422: step 7500, loss = 1.086305 (33.4 examples/sec)\
=> 2018-12-15 00:52:40.583529: step 7600, loss = 0.184690 (33.4 examples/sec)\
=> 2018-12-15 00:54:16.840546: step 7700, loss = 0.466766 (33.2 examples/sec)\
=> 2018-12-15 00:55:52.799016: step 7800, loss = 0.326159 (33.3 examples/sec)\
=> 2018-12-15 00:57:28.605812: step 7900, loss = 0.943777 (33.4 examples/sec)\
=> 2018-12-15 00:59:04.928255: step 8000, loss = 0.514754 (33.2 examples/sec)\
=> Model saved to file: ./logs/train/model.ckpt-8000\
=> patience = 100\
=> 2018-12-15 01:03:41.988285: step 8100, loss = 0.991954 (33.4 examples/sec)\
=> 2018-12-15 01:05:18.187992: step 8200, loss = 1.293353 (33.3 examples/sec)\
=> 2018-12-15 01:06:54.056409: step 8300, loss = 0.231978 (33.4 examples/sec)\
=> 2018-12-15 01:08:29.769291: step 8400, loss = 0.868102 (33.4 examples/sec)\
=> 2018-12-15 01:10:06.077136: step 8500, loss = 0.456693 (33.2 examples/sec)\
=> 2018-12-15 01:11:41.410785: step 8600, loss = 1.144073 (33.6 examples/sec)\
=> 2018-12-15 01:13:16.960310: step 8700, loss = 1.401476 (33.5 examples/sec)\
=> 2018-12-15 01:14:52.773643: step 8800, loss = 0.271077 (33.4 examples/sec)\
=> 2018-12-15 01:16:28.089578: step 8900, loss = 0.741466 (33.6 examples/sec)\
=> 2018-12-15 01:18:03.410101: step 9000, loss = 0.637775 (33.6 examples/sec)\
=> 2018-12-15 01:22:39.449781: step 9100, loss = 0.589976 (33.6 examples/sec)\
=> 2018-12-15 01:24:14.923988: step 9200, loss = 0.421387 (33.5 examples/sec)\
=> 2018-12-15 01:25:50.916771: step 9300, loss = 0.319450 (33.3 examples/sec)\
=> 2018-12-15 01:27:26.076317: step 9400, loss = 0.502507 (33.6 examples/sec)\
=> 2018-12-15 01:29:01.183197: step 9500, loss = 0.739275 (33.6 examples/sec)\
=> 2018-12-15 01:30:37.016866: step 9600, loss = 0.623278 (33.4 examples/sec)\
=> 2018-12-15 01:32:12.330014: step 9700, loss = 0.846131 (33.6 examples/sec)\
=> 2018-12-15 01:33:47.489583: step 9800, loss = 0.742466 (33.6 examples/sec)\
=> 2018-12-15 01:35:23.254234: step 9900, loss = 0.177544 (33.4 examples/sec)\
=> 2018-12-15 01:36:58.549766: step 10000, loss = 1.030436 (33.6 examples/sec)\
2018-12-15 03:22:59.865257: step 10100, loss = 0.259781 (28.9 examples/sec)\
=> 2018-12-15 03:24:37.450800: step 10200, loss = 1.014183 (32.8 examples/sec)\
=> 2018-12-15 03:26:15.303018: step 10300, loss = 0.195970 (32.7 examples/sec)\
=> 2018-12-15 03:27:52.746398: step 10400, loss = 0.727002 (32.8 examples/sec)\
=> 2018-12-15 03:29:30.170757: step 10500, loss = 0.263290 (32.8 examples/sec)\
=> 2018-12-15 03:31:07.404642: step 10600, loss = 0.470597 (32.9 examples/sec)\
=> 2018-12-15 03:32:45.059906: step 10700, loss = 1.028347 (32.8 examples/sec)\
=> 2018-12-15 03:34:22.542187: step 10800, loss = 0.609772 (32.8 examples/sec)\
=> 2018-12-15 03:35:59.738099: step 10900, loss = 0.488388 (32.9 examples/sec)\
=> 2018-12-15 03:37:37.372023: step 11000, loss = 1.374107 (32.8 examples/sec)\
==> accuracy = 0.891389, best accuracy 0.000000\
=> Model saved to file: ./logs/train/model.ckpt-11000\
=> patience = 100\
=> 2018-12-15 03:42:21.808935: step 11100, loss = 0.704416 (32.8 examples/sec)\
=> 2018-12-15 03:43:59.082330: step 11200, loss = 1.047571 (32.9 examples/sec)\
=> 2018-12-15 03:45:36.594608: step 11300, loss = 1.071276 (32.8 examples/sec)\
=> 2018-12-15 03:47:14.334146: step 11400, loss = 1.198133 (32.7 examples/sec)\
=> 2018-12-15 03:48:51.678548: step 11500, loss = 0.323369 (32.9 examples/sec)\
=> 2018-12-15 03:50:29.076233: step 11600, loss = 0.770093 (32.9 examples/sec)\
=> 2018-12-15 03:52:06.776206: step 11700, loss = 0.497296 (32.8 examples/sec)\
=> 2018-12-15 03:53:44.211581: step 11800, loss = 0.768522 (32.8 examples/sec)\
=> 2018-12-15 03:55:21.850480: step 11900, loss = 0.573841 (32.8 examples/sec)\
=> 2018-12-15 03:56:59.356076: step 12000, loss = 0.379566 (32.8 examples/sec)\
\
==> accuracy = 0.902683, best accuracy 0.891389\
\
=> 2018-12-15 04:01:41.908698: step 12100, loss = 1.494554 (32.8 examples/sec)\
=> 2018-12-15 04:03:19.801259: step 12200, loss = 0.233663 (32.7 examples/sec)\
=> 2018-12-15 04:04:57.479347: step 12300, loss = 0.844735 (32.8 examples/sec)\
=> 2018-12-15 04:06:35.013519: step 12400, loss = 1.190445 (32.8 examples/sec)\
=> 2018-12-15 04:08:12.787422: step 12500, loss = 0.260971 (32.7 examples/sec)\
=> 2018-12-15 04:09:50.433415: step 12600, loss = 0.095614 (32.8 examples/sec)\
=> 2018-12-15 04:11:27.767155: step 12700, loss = 0.583264 (32.9 examples/sec)\
=> 2018-12-15 04:13:05.442705: step 12800, loss = 0.392390 (32.8 examples/sec)\
=> 2018-12-15 04:14:42.864933: step 12900, loss = 0.715849 (32.8 examples/sec)\
=> 2018-12-15 04:16:20.533169: step 13000, loss = 0.354944 (32.8 examples/sec)\
==> accuracy = 0.903320, best accuracy 0.902683\
=> Model saved to file: ./logs/train/model.ckpt-13000\
=> patience = 100\
=> 2018-12-15 04:21:03.361011: step 13100, loss = 0.236832 (32.8 examples/sec)\
=> 2018-12-15 04:22:40.809869: step 13200, loss = 0.288215 (32.8 examples/sec)\
=> 2018-12-15 04:24:18.342633: step 13300, loss = 0.391643 (32.8 examples/sec)\
=> 2018-12-15 04:25:55.737514: step 13400, loss = 0.908231 (32.9 examples/sec)\
=> 2018-12-15 04:27:33.022460: step 13500, loss = 0.276314 (32.9 examples/sec)\
=> 2018-12-15 04:29:10.527586: step 13600, loss = 0.276509 (32.8 examples/sec)\
=> 2018-12-15 04:30:47.947503: step 13700, loss = 0.236634 (32.8 examples/sec)\
=> 2018-12-15 04:32:25.075390: step 13800, loss = 0.786826 (32.9 examples/sec)\
=> 2018-12-15 04:34:02.510727: step 13900, loss = 0.486508 (32.8 examples/sec)\
=> 2018-12-15 04:35:39.746386: step 14000, loss = 0.195844 (32.9 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.900603, best accuracy 0.903320\
=> patience = 99\
=> 2018-12-15 04:40:22.735094: step 14100, loss = 1.303165 (32.8 examples/sec)\
=> 2018-12-15 04:41:59.974757: step 14200, loss = 0.861559 (32.9 examples/sec)\
=> 2018-12-15 04:43:37.156927: step 14300, loss = 1.461068 (32.9 examples/sec)\
=> 2018-12-15 04:45:14.658516: step 14400, loss = 0.218920 (32.8 examples/sec)\
=> 2018-12-15 04:46:52.041873: step 14500, loss = 0.318557 (32.9 examples/sec)\
=> 2018-12-15 04:48:29.280557: step 14600, loss = 0.494588 (32.9 examples/sec)\
=> 2018-12-15 04:50:06.732183: step 14700, loss = 0.974542 (32.8 examples/sec)\
=> 2018-12-15 04:51:44.014321: step 14800, loss = 0.330649 (32.9 examples/sec)\
=> 2018-12-15 04:53:21.141564: step 14900, loss = 0.979146 (32.9 examples/sec)\
=> 2018-12-15 04:54:58.615397: step 15000, loss = 0.371111 (32.8 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.912789, best accuracy 0.903320\
=> Model saved to file: ./logs/train/model.ckpt-15000\
=> patience = 100\
=> 2018-12-15 04:59:42.167348: step 15100, loss = 1.097210 (32.9 examples/sec)\
=> 2018-12-15 05:01:19.419277: step 15200, loss = 0.694337 (32.9 examples/sec)\
=> 2018-12-15 05:02:56.453599: step 15300, loss = 0.356857 (33.0 examples/sec)\
=> 2018-12-15 05:04:33.885287: step 15400, loss = 0.528054 (32.8 examples/sec)\
=> 2018-12-15 05:06:11.200090: step 15500, loss = 0.215169 (32.9 examples/sec)\
=> 2018-12-15 05:07:48.333681: step 15600, loss = 1.033262 (32.9 examples/sec)\
=> 2018-12-15 05:09:25.479752: step 15700, loss = 0.864478 (32.9 examples/sec)\
=> 2018-12-15 05:11:03.140154: step 15800, loss = 0.574057 (32.8 examples/sec)\
=> 2018-12-15 05:12:40.002353: step 15900, loss = 0.914138 (33.0 examples/sec)\
=> 2018-12-15 05:14:16.897249: step 16000, loss = 0.389949 (33.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.910836, best accuracy 0.912789\
=> patience = 99\
=> 2018-12-15 05:18:59.662654: step 16100, loss = 0.720741 (33.0 examples/sec)\
=> 2018-12-15 05:20:36.913051: step 16200, loss = 0.232342 (32.9 examples/sec)\
=> 2018-12-15 05:22:13.919997: step 16300, loss = 0.421583 (33.0 examples/sec)\
=> 2018-12-15 05:23:50.801352: step 16400, loss = 1.175818 (33.0 examples/sec)\
=> 2018-12-15 05:25:28.021453: step 16500, loss = 0.451488 (32.9 examples/sec)\
=> 2018-12-15 05:27:05.091755: step 16600, loss = 1.587662 (33.0 examples/sec)\
=> 2018-12-15 05:28:42.048259: step 16700, loss = 0.778611 (33.0 examples/sec)\
=> 2018-12-15 05:30:19.209223: step 16800, loss = 0.331891 (32.9 examples/sec)\
=> 2018-12-15 05:31:56.357289: step 16900, loss = 0.393058 (32.9 examples/sec)\
=> 2018-12-15 05:33:33.337097: step 17000, loss = 2.009481 (33.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.910241, best accuracy 0.912789\
=> patience = 98\
=> 2018-12-15 05:38:14.091379: step 17100, loss = 0.432662 (33.0 examples/sec)\
=> 2018-12-15 05:39:50.945618: step 17200, loss = 0.289731 (33.0 examples/sec)\
=> 2018-12-15 05:41:28.346504: step 17300, loss = 2.426907 (32.9 examples/sec)\
=> 2018-12-15 05:43:05.319257: step 17400, loss = 0.601128 (33.0 examples/sec)\
=> 2018-12-15 05:44:42.241918: step 17500, loss = 0.981230 (33.0 examples/sec)\
=> 2018-12-15 05:46:19.413794: step 17600, loss = 0.113240 (32.9 examples/sec)\
=> 2018-12-15 05:47:56.480983: step 17700, loss = 0.681106 (33.0 examples/sec)\
=> 2018-12-15 05:49:33.267070: step 17800, loss = 0.529427 (33.1 examples/sec)\
=> 2018-12-15 05:51:10.389930: step 17900, loss = 0.311564 (32.9 examples/sec)\
=> 2018-12-15 05:52:47.408861: step 18000, loss = 0.097307 (33.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.915591, best accuracy 0.912789\
=> Model saved to file: ./logs/train/model.ckpt-18000\
=> patience = 100\
=> 2018-12-15 05:57:28.852348: step 18100, loss = 0.136254 (32.8 examples/sec)\
=> 2018-12-15 05:59:05.823910: step 18200, loss = 0.536392 (33.0 examples/sec)\
=> 2018-12-15 06:00:42.793988: step 18300, loss = 0.524068 (33.0 examples/sec)\
=> 2018-12-15 06:02:20.278286: step 18400, loss = 0.130738 (32.8 examples/sec)\
=> 2018-12-15 06:03:57.316059: step 18500, loss = 0.255802 (33.0 examples/sec)\
=> 2018-12-15 06:05:34.247192: step 18600, loss = 0.291012 (33.0 examples/sec)\
=> 2018-12-15 06:07:11.628903: step 18700, loss = 0.652625 (32.9 examples/sec)\
=> 2018-12-15 06:08:48.553658: step 18800, loss = 0.610042 (33.0 examples/sec)\
=> 2018-12-15 06:10:25.405073: step 18900, loss = 0.088005 (33.0 examples/sec)\
=> 2018-12-15 06:12:02.894575: step 19000, loss = 1.880871 (32.8 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.918054, best accuracy 0.915591\
=> Model saved to file: ./logs/train/model.ckpt-19000\
=> patience = 100\
=> 2018-12-15 06:16:43.780609: step 19100, loss = 0.218312 (33.0 examples/sec)\
=> 2018-12-15 06:18:21.422151: step 19200, loss = 0.094290 (32.8 examples/sec)\
=> 2018-12-15 06:19:58.414952: step 19300, loss = 0.432366 (33.0 examples/sec)\
=> 2018-12-15 06:21:35.408551: step 19400, loss = 0.172733 (33.0 examples/sec)\
=> 2018-12-15 06:23:13.093710: step 19500, loss = 0.416325 (32.8 examples/sec)\
=> 2018-12-15 06:24:50.139451: step 19600, loss = 0.298524 (33.0 examples/sec)\
=> 2018-12-15 06:26:28.523976: step 19700, loss = 0.140768 (32.5 examples/sec)\
=> 2018-12-15 06:28:06.206496: step 19800, loss = 0.096149 (32.8 examples/sec)\
=> 2018-12-15 06:29:43.294622: step 19900, loss = 0.117915 (33.0 examples/sec)\
=> 2018-12-15 06:31:20.385483: step 20000, loss = 0.396437 (33.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.917926, best accuracy 0.918054\
=> 2018-12-15 13:18:56.803107: step 20100, loss = 0.144564 (32.2 examples/sec)\
=> 2018-12-15 13:20:35.295182: step 20200, loss = 0.502809 (32.5 examples/sec)\
=> 2018-12-15 13:22:14.697178: step 20300, loss = 0.590478 (32.2 examples/sec)\
=> 2018-12-15 13:23:54.200692: step 20400, loss = 0.126437 (32.2 examples/sec)\
=> 2018-12-15 13:25:32.754943: step 20500, loss = 0.374593 (32.5 examples/sec)\
=> 2018-12-15 13:27:12.623038: step 20600, loss = 0.342957 (32.0 examples/sec)\
=> 2018-12-15 13:28:51.709319: step 20700, loss = 0.793741 (32.3 examples/sec)\
=> 2018-12-15 13:30:30.437552: step 20800, loss = 0.365978 (32.4 examples/sec)\
=> 2018-12-15 13:32:10.292041: step 20900, loss = 0.300126 (32.0 examples/sec)\
=> 2018-12-15 13:33:49.001266: step 21000, loss = 1.052495 (32.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.928626, best accuracy 0.920686\
=> Model saved to file: ./logs/train/model.ckpt-21000\
=> patience = 100\
=> 2018-12-15 13:38:33.537791: step 21100, loss = 0.757618 (32.6 examples/sec)\
=> 2018-12-15 13:40:13.171806: step 21200, loss = 0.146723 (32.1 examples/sec)\
=> 2018-12-15 13:41:52.057938: step 21300, loss = 0.117969 (32.4 examples/sec)\
=> 2018-12-15 13:43:31.765096: step 21400, loss = 0.208423 (32.1 examples/sec)\
=> 2018-12-15 13:45:11.537829: step 21500, loss = 0.353376 (32.1 examples/sec)\
=> 2018-12-15 13:46:51.575381: step 21600, loss = 0.316501 (32.0 examples/sec)\
=> 2018-12-15 13:48:31.389984: step 21700, loss = 0.109646 (32.1 examples/sec)\
=> 2018-12-15 13:50:10.833890: step 21800, loss = 0.339611 (32.2 examples/sec)\
=> 2018-12-15 13:51:50.205158: step 21900, loss = 0.939086 (32.2 examples/sec)\
=> 2018-12-15 13:53:28.749866: step 22000, loss = 0.296197 (32.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.925357, best accuracy 0.928626\
=> patience = 99\
=> 2018-12-15 13:58:13.974182: step 22100, loss = 0.038183 (32.2 examples/sec)\
=> 2018-12-15 13:59:53.340897: step 22200, loss = 0.605044 (32.2 examples/sec)\
=> 2018-12-15 14:01:32.136822: step 22300, loss = 0.318702 (32.4 examples/sec)\
=> 2018-12-15 14:03:11.496725: step 22400, loss = 1.973912 (32.2 examples/sec)\
=> 2018-12-15 14:04:51.012901: step 22500, loss = 0.213322 (32.2 examples/sec)\
=> 2018-12-15 14:06:29.481344: step 22600, loss = 0.597535 (32.5 examples/sec)\
=> 2018-12-15 14:08:09.425298: step 22700, loss = 0.187995 (32.0 examples/sec)\
=> 2018-12-15 14:09:48.918491: step 22800, loss = 0.229212 (32.2 examples/sec)\
=> 2018-12-15 14:11:27.505840: step 22900, loss = 0.196660 (32.5 examples/sec)\
=> 2018-12-15 14:13:07.462186: step 23000, loss = 0.565315 (32.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.926078, best accuracy 0.928626\
=> patience = 98\
=> 2018-12-15 14:17:53.328189: step 23100, loss = 0.046229 (31.9 examples/sec)\
=> 2018-12-15 14:19:32.472917: step 23200, loss = 0.305737 (32.3 examples/sec)\
=> 2018-12-15 14:21:12.019804: step 23300, loss = 0.370723 (32.1 examples/sec)\
=> 2018-12-15 14:22:51.437312: step 23400, loss = 0.560856 (32.2 examples/sec)\
=> 2018-12-15 14:24:29.933464: step 23500, loss = 0.547509 (32.5 examples/sec)\
=> 2018-12-15 14:26:09.629455: step 23600, loss = 0.362149 (32.1 examples/sec)\
=> 2018-12-15 14:27:48.645513: step 23700, loss = 0.512540 (32.3 examples/sec)\
=> 2018-12-15 14:29:27.498336: step 23800, loss = 1.323534 (32.4 examples/sec)\
=> 2018-12-15 14:31:07.026238: step 23900, loss = 0.424035 (32.2 examples/sec)\
=> 2018-12-15 14:32:45.560386: step 24000, loss = 0.112703 (32.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.927310, best accuracy 0.928626\
=> patience = 97\
=> 2018-12-15 14:37:31.079205: step 24100, loss = 1.199638 (32.1 examples/sec)\
=> 2018-12-15 14:39:10.834576: step 24200, loss = 0.584933 (32.1 examples/sec)\
=> 2018-12-15 14:40:50.866439: step 24300, loss = 0.367592 (32.0 examples/sec)\
=> 2018-12-15 14:42:30.571260: step 24400, loss = 0.460415 (32.1 examples/sec)\
=> 2018-12-15 14:44:09.893897: step 24500, loss = 0.190997 (32.2 examples/sec)\
=> 2018-12-15 14:45:49.328812: step 24600, loss = 0.383912 (32.2 examples/sec)\
=> 2018-12-15 14:47:27.581606: step 24700, loss = 0.919055 (32.6 examples/sec)\
=> 2018-12-15 14:49:07.334614: step 24800, loss = 0.301963 (32.1 examples/sec)\
=> 2018-12-15 14:50:46.621211: step 24900, loss = 0.604990 (32.2 examples/sec)\
=> 2018-12-15 14:52:25.321018: step 25000, loss = 0.390229 (32.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.926121, best accuracy 0.928626\
=> patience = 96\
=> 2018-12-15 14:57:12.215367: step 25100, loss = 0.592545 (32.3 examples/sec)\
=> 2018-12-15 14:58:51.318243: step 25200, loss = 1.079815 (32.3 examples/sec)\
=> 2018-12-15 15:00:29.459687: step 25300, loss = 0.262859 (32.6 examples/sec)\
=> 2018-12-15 15:02:08.703710: step 25400, loss = 0.078463 (32.2 examples/sec)\
=> 2018-12-15 15:03:47.246315: step 25500, loss = 0.242474 (32.5 examples/sec)\
=> 2018-12-15 15:05:25.754690: step 25600, loss = 0.673741 (32.5 examples/sec)\
=> 2018-12-15 15:07:04.872254: step 25700, loss = 0.169784 (32.3 examples/sec)\
=> 2018-12-15 15:08:42.982838: step 25800, loss = 0.268861 (32.6 examples/sec)\
=> 2018-12-15 15:10:21.994556: step 25900, loss = 0.351026 (32.3 examples/sec)\
=> 2018-12-15 15:12:01.246732: step 26000, loss = 0.541122 (32.2 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.932872, best accuracy 0.928626\
=> 2018-12-15 16:11:47.980700: step 26100, loss = 0.499550 (29.4 examples/sec)\
=> 2018-12-15 16:13:23.731649: step 26200, loss = 0.137367 (33.4 examples/sec)\
=> 2018-12-15 16:14:59.363069: step 26300, loss = 0.684537 (33.5 examples/sec)\
=> 2018-12-15 16:16:34.872926: step 26400, loss = 0.249522 (33.5 examples/sec)\
=> 2018-12-15 16:18:10.678758: step 26500, loss = 0.677295 (33.4 examples/sec)\
=> 2018-12-15 16:19:46.464019: step 26600, loss = 0.502070 (33.4 examples/sec)\
=> 2018-12-15 16:21:21.892768: step 26700, loss = 0.278915 (33.5 examples/sec)\
=> 2018-12-15 16:22:57.629445: step 26800, loss = 0.453131 (33.4 examples/sec)\
=> 2018-12-15 16:24:33.278833: step 26900, loss = 1.213394 (33.5 examples/sec)\
=> 2018-12-15 16:26:08.758918: step 27000, loss = 0.087553 (33.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.930579, best accuracy 0.000000\
=> Model saved to file: ./logs/train/model.ckpt-27000\
=> patience = 100\
=> 2018-12-15 16:30:49.514850: step 27100, loss = 0.836841 (33.6 examples/sec)\
=> 2018-12-15 16:32:24.717073: step 27200, loss = 0.279186 (33.6 examples/sec)\
=> 2018-12-15 16:34:00.491076: step 27300, loss = 0.245629 (33.4 examples/sec)\
=> 2018-12-15 16:35:36.056888: step 27400, loss = 0.591749 (33.5 examples/sec)\
=> 2018-12-15 16:37:11.511721: step 27500, loss = 0.104853 (33.5 examples/sec)\
=> 2018-12-15 16:38:47.415707: step 27600, loss = 0.659299 (33.4 examples/sec)\
=> 2018-12-15 16:40:22.879738: step 27700, loss = 0.992741 (33.5 examples/sec)\
=> 2018-12-15 16:41:58.476117: step 27800, loss = 0.050762 (33.5 examples/sec)\
=> 2018-12-15 16:43:34.292227: step 27900, loss = 0.399944 (33.4 examples/sec)\
=> 2018-12-15 16:45:09.948260: step 28000, loss = 0.253342 (33.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.927777, best accuracy 0.930579\
=> patience = 99\
=> 2018-12-15 16:49:46.671659: step 28100, loss = 0.573927 (33.4 examples/sec)\
=> 2018-12-15 16:51:22.137514: step 28200, loss = 0.261956 (33.5 examples/sec)\
=> 2018-12-15 16:52:57.540937: step 28300, loss = 0.130844 (33.5 examples/sec)\
=> 2018-12-15 16:54:33.492029: step 28400, loss = 0.543614 (33.4 examples/sec)\
=> 2018-12-15 16:56:09.123680: step 28500, loss = 0.458966 (33.5 examples/sec)\
=> 2018-12-15 16:57:44.810899: step 28600, loss = 0.091690 (33.4 examples/sec)\
=> 2018-12-15 16:59:20.901702: step 28700, loss = 0.466423 (33.3 examples/sec)\
=> 2018-12-15 17:00:56.563608: step 28800, loss = 0.268229 (33.5 examples/sec)\
=> 2018-12-15 17:02:32.196722: step 28900, loss = 0.051421 (33.5 examples/sec)\
=> 2018-12-15 17:04:08.271048: step 29000, loss = 1.177383 (33.3 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.924295, best accuracy 0.930579\
=> patience = 98\
=> 2018-12-15 17:08:44.982232: step 29100, loss = 0.114970 (33.4 examples/sec)\
=> 2018-12-15 17:10:20.884773: step 29200, loss = 0.218740 (33.4 examples/sec)\
=> 2018-12-15 17:11:56.275823: step 29300, loss = 0.231191 (33.5 examples/sec)\
=> 2018-12-15 17:13:31.609430: step 29400, loss = 0.077762 (33.6 examples/sec)\
=> 2018-12-15 17:15:07.606640: step 29500, loss = 0.653717 (33.3 examples/sec)\
=> 2018-12-15 17:16:43.125273: step 29600, loss = 0.922382 (33.5 examples/sec)\
=> 2018-12-15 17:18:18.639710: step 29700, loss = 0.145871 (33.5 examples/sec)\
=> 2018-12-15 17:19:54.707481: step 29800, loss = 0.032098 (33.3 examples/sec)\
=> 2018-12-15 17:21:30.376374: step 29900, loss = 0.133990 (33.5 examples/sec)\
=> 2018-12-15 17:23:06.033303: step 30000, loss = 0.487789 (33.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.932405, best accuracy 0.930579\
=> Model saved to file: ./logs/train/model.ckpt-30000\
=> patience = 100\
=> 2018-12-15 17:27:44.469603: step 30100, loss = 0.277335 (33.5 examples/sec)\
=> 2018-12-15 17:29:19.939793: step 30200, loss = 0.751926 (33.5 examples/sec)\
=> 2018-12-15 17:30:55.697112: step 30300, loss = 0.203137 (33.4 examples/sec)\
=> 2018-12-15 17:32:30.821079: step 30400, loss = 0.067784 (33.6 examples/sec)\
=> 2018-12-15 17:34:05.766408: step 30500, loss = 0.055553 (33.7 examples/sec)\
=> 2018-12-15 17:35:41.270916: step 30600, loss = 0.584055 (33.5 examples/sec)\
=> 2018-12-15 17:37:16.152638: step 30700, loss = 0.372657 (33.7 examples/sec)\
=> 2018-12-15 17:38:51.067063: step 30800, loss = 0.261895 (33.7 examples/sec)\
=> 2018-12-15 17:40:26.563065: step 30900, loss = 0.305527 (33.5 examples/sec)\
=> 2018-12-15 17:42:01.444384: step 31000, loss = 0.122672 (33.7 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.929815, best accuracy 0.932405\
=> patience = 99\
=> 2018-12-15 17:46:39.025232: step 31100, loss = 0.129510 (33.4 examples/sec)\
=> 2018-12-15 17:48:14.525340: step 31200, loss = 0.342312 (33.5 examples/sec)\
=> 2018-12-15 17:49:50.009461: step 31300, loss = 0.597607 (33.5 examples/sec)\
=> 2018-12-15 17:51:25.859779: step 31400, loss = 0.098471 (33.4 examples/sec)\
=> 2018-12-15 17:53:01.108969: step 31500, loss = 0.140662 (33.6 examples/sec)\
=> 2018-12-15 17:54:36.711844: step 31600, loss = 0.245591 (33.5 examples/sec)\
=> 2018-12-15 17:56:12.534461: step 31700, loss = 0.129069 (33.4 examples/sec)\
=> 2018-12-15 17:57:48.015305: step 31800, loss = 0.453519 (33.5 examples/sec)\
=> 2018-12-15 17:59:23.499382: step 31900, loss = 0.286992 (33.5 examples/sec)\
=> 2018-12-15 18:00:59.386226: step 32000, loss = 0.383698 (33.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.935717, best accuracy 0.932405\
=> Model saved to file: ./logs/train/model.ckpt-32000\
=> patience = 100\
=> 2018-12-15 18:05:36.416006: step 32100, loss = 0.679192 (33.5 examples/sec)\
=> 2018-12-15 18:07:12.117877: step 32200, loss = 0.224270 (33.4 examples/sec)\
=> 2018-12-15 18:08:47.564922: step 32300, loss = 0.141271 (33.5 examples/sec)\
=> 2018-12-15 18:10:23.119418: step 32400, loss = 0.763360 (33.5 examples/sec)\
=> 2018-12-15 18:11:58.718921: step 32500, loss = 0.043354 (33.5 examples/sec)\
=> 2018-12-15 18:13:34.072983: step 32600, loss = 0.334474 (33.6 examples/sec)\
=> 2018-12-15 18:15:09.674971: step 32700, loss = 0.124399 (33.5 examples/sec)\
=> 2018-12-15 18:16:45.657208: step 32800, loss = 0.435485 (33.3 examples/sec)\
=> 2018-12-15 18:18:21.287540: step 32900, loss = 0.226623 (33.5 examples/sec)\
=> 2018-12-15 18:19:56.932035: step 33000, loss = 0.239685 (33.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.931726, best accuracy 0.935717\
=> patience = 99\
=> 2018-12-15 18:24:33.614371: step 33100, loss = 0.141156 (33.5 examples/sec)\
=> 2018-12-15 18:26:09.380349: step 33200, loss = 0.009262 (33.4 examples/sec)\
=> 2018-12-15 18:27:45.222422: step 33300, loss = 0.386125 (33.4 examples/sec)\
=> 2018-12-15 18:29:20.873751: step 33400, loss = 0.391422 (33.5 examples/sec)\
=> 2018-12-15 18:30:56.376832: step 33500, loss = 0.208407 (33.5 examples/sec)\
=> 2018-12-15 18:32:31.860900: step 33600, loss = 0.219896 (33.5 examples/sec)\
=> 2018-12-15 18:34:07.211355: step 33700, loss = 0.146658 (33.6 examples/sec)\
=> 2018-12-15 18:35:42.720704: step 33800, loss = 0.023004 (33.5 examples/sec)\
=> 2018-12-15 18:37:18.457927: step 33900, loss = 0.124304 (33.4 examples/sec)\
=> 2018-12-15 18:38:53.848968: step 34000, loss = 0.197536 (33.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.934443, best accuracy 0.935717\
=> 2018-12-15 19:03:07.380105: step 34100, loss = 0.317783 (29.1 examples/sec)\
=> 2018-12-15 19:04:43.100991: step 34200, loss = 0.394641 (33.4 examples/sec)\
=> 2018-12-15 19:06:18.851604: step 34300, loss = 0.020762 (33.4 examples/sec)\
=> 2018-12-15 19:07:54.623355: step 34400, loss = 0.086570 (33.4 examples/sec)\
=> 2018-12-15 19:09:30.083522: step 34500, loss = 0.556472 (33.5 examples/sec)\
=> 2018-12-15 19:11:05.427525: step 34600, loss = 0.153756 (33.6 examples/sec)\
=> 2018-12-15 19:12:41.189188: step 34700, loss = 0.474246 (33.4 examples/sec)\
=> 2018-12-15 19:14:17.044538: step 34800, loss = 0.034674 (33.4 examples/sec)\
=> 2018-12-15 19:15:52.670021: step 34900, loss = 0.151729 (33.5 examples/sec)\
=> 2018-12-15 19:17:28.356989: step 35000, loss = 0.045741 (33.4 examples/sec)\
=> Evaluating on validation dataset...\
accuracy = 0.936821, best accuracy 0.000000\
"

model_text_1="\
=> 2018-12-17 01:16:26.018407: step 100, loss = 7.291442 (34.4 examples/sec)\
=> 2018-12-17 01:17:40.995242: step 200, loss = 7.092419 (42.7 examples/sec)\
=> 2018-12-17 01:18:55.886351: step 300, loss = 6.835694 (42.7 examples/sec)\
=> 2018-12-17 01:20:10.623824: step 400, loss = 6.594741 (42.8 examples/sec)\
=> 2018-12-17 01:21:25.815795: step 500, loss = 6.762383 (42.6 examples/sec)\
=> 2018-12-17 01:22:41.676224: step 600, loss = 6.805425 (42.2 examples/sec)\
=> 2018-12-17 01:23:56.954693: step 700, loss = 5.737284 (42.5 examples/sec)\
=> 2018-12-17 01:25:12.055698: step 800, loss = 6.512980 (42.6 examples/sec)\
=> 2018-12-17 01:26:27.543290: step 900, loss = 5.918442 (42.4 examples/sec)\
=> 2018-12-17 01:27:43.100393: step 1000, loss = 5.995659 (42.4 examples/sec)\
==> accuracy = 0.060557, best accuracy 0.000000\
=> 2018-12-17 01:31:05.395436: step 1100, loss = 5.129948 (42.1 examples/sec)\
=> 2018-12-17 01:32:21.585958: step 1200, loss = 5.257332 (42.0 examples/sec)\
=> 2018-12-17 01:33:38.139111: step 1300, loss = 4.308627 (41.8 examples/sec)\
=> 2018-12-17 01:34:53.998314: step 1400, loss = 5.118458 (42.2 examples/sec)\
=> 2018-12-17 01:36:09.450521: step 1500, loss = 3.670438 (42.4 examples/sec)\
=> 2018-12-17 01:37:24.870519: step 1600, loss = 3.749571 (42.4 examples/sec)\
=> 2018-12-17 01:38:40.256665: step 1700, loss = 2.861261 (42.5 examples/sec)\
=> 2018-12-17 01:39:55.530542: step 1800, loss = 3.015757 (42.5 examples/sec)\
=> 2018-12-17 01:41:10.638962: step 1900, loss = 2.127000 (42.6 examples/sec)\
=> 2018-12-17 01:42:25.933332: step 2000, loss = 2.531801 (42.5 examples/sec)\
==> accuracy = 0.472593, best accuracy 0.060557\
=> 2018-12-17 01:45:49.443867: step 2100, loss = 1.794385 (42.4 examples/sec)\
=> 2018-12-17 01:47:04.887792: step 2200, loss = 2.361413 (42.4 examples/sec)\
=> 2018-12-17 01:48:20.341051: step 2300, loss = 1.761110 (42.4 examples/sec)\
=> 2018-12-17 01:49:36.232934: step 2400, loss = 0.908026 (42.2 examples/sec)\
=> 2018-12-17 01:50:51.470554: step 2500, loss = 1.332543 (42.5 examples/sec)\
=> 2018-12-17 01:52:07.069209: step 2600, loss = 1.145427 (42.3 examples/sec)\
=> 2018-12-17 01:53:22.589561: step 2700, loss = 2.227424 (42.4 examples/sec)\
=> 2018-12-17 01:54:38.101756: step 2800, loss = 1.184182 (42.4 examples/sec)\
=> 2018-12-17 01:55:53.502858: step 2900, loss = 2.249053 (42.4 examples/sec)\
=> 2018-12-17 01:57:08.910262: step 3000, loss = 0.850076 (42.4 examples/sec)\
==> accuracy = 0.720017, best accuracy 0.472593\
=> 2018-12-17 02:00:32.669377: step 3100, loss = 1.312922 (42.3 examples/sec)\
=> 2018-12-17 02:01:48.314887: step 3200, loss = 1.528227 (42.3 examples/sec)\
=> 2018-12-17 02:03:03.869215: step 3300, loss = 1.519447 (42.4 examples/sec)\
=> 2018-12-17 02:04:19.815211: step 3400, loss = 2.493637 (42.1 examples/sec)\
=> 2018-12-17 02:05:35.713832: step 3500, loss = 1.706139 (42.2 examples/sec)\
=> 2018-12-17 02:06:51.430100: step 3600, loss = 2.348182 (42.3 examples/sec)\
=> 2018-12-17 02:08:07.701634: step 3700, loss = 2.324250 (42.0 examples/sec)\
=> 2018-12-17 02:09:23.760764: step 3800, loss = 2.239961 (42.1 examples/sec)\
=> 2018-12-17 02:10:39.485071: step 3900, loss = 0.925004 (42.3 examples/sec)\
=> 2018-12-17 02:11:55.190377: step 4000, loss = 2.427018 (42.3 examples/sec)\
==> accuracy = 0.795439, best accuracy 0.720017\
=> 2018-12-17 02:15:19.345458: step 4100, loss = 1.333530 (42.1 examples/sec)\
=> 2018-12-17 02:16:35.069484: step 4200, loss = 0.818768 (42.3 examples/sec)\
=> 2018-12-17 02:17:50.605544: step 4300, loss = 0.169471 (42.4 examples/sec)\
=> 2018-12-17 02:19:05.990801: step 4400, loss = 1.402747 (42.5 examples/sec)\
=> 2018-12-17 02:20:21.378146: step 4500, loss = 0.942520 (42.4 examples/sec)\
=> 2018-12-17 02:21:36.579707: step 4600, loss = 1.120772 (42.6 examples/sec)\
=> 2018-12-17 02:22:51.861189: step 4700, loss = 0.836317 (42.5 examples/sec)\
=> 2018-12-17 02:24:06.848879: step 4800, loss = 1.555599 (42.7 examples/sec)\
=> 2018-12-17 02:25:21.971898: step 4900, loss = 1.011759 (42.6 examples/sec)\
=> 2018-12-17 02:26:36.753407: step 5000, loss = 1.133267 (42.8 examples/sec)\
==> accuracy = 0.829814, best accuracy 0.795439\
=> 2018-12-17 02:29:58.879170: step 5100, loss = 0.744653 (42.5 examples/sec)\
=> 2018-12-17 02:31:14.658460: step 5200, loss = 1.912119 (42.2 examples/sec)\
=> 2018-12-17 02:32:30.365758: step 5300, loss = 0.557806 (42.3 examples/sec)\
=> 2018-12-17 02:33:45.864479: step 5400, loss = 0.882001 (42.4 examples/sec)\
=> 2018-12-17 02:35:01.420475: step 5500, loss = 0.422280 (42.4 examples/sec)\
=> 2018-12-17 02:36:17.302109: step 5600, loss = 0.678243 (42.2 examples/sec)\
=> 2018-12-17 02:37:33.029398: step 5700, loss = 1.175826 (42.3 examples/sec)\
=> 2018-12-17 02:38:48.963250: step 5800, loss = 0.184411 (42.1 examples/sec)\
=> 2018-12-17 02:40:04.652809: step 5900, loss = 0.969176 (42.3 examples/sec)\
=> 2018-12-17 02:41:20.718941: step 6000, loss = 0.628747 (42.1 examples/sec)\
==> accuracy = 0.855870, best accuracy 0.829814\
=> 2018-12-17 02:44:45.246397: step 6100, loss = 0.564970 (42.0 examples/sec)\
=> 2018-12-17 02:46:01.153390: step 6200, loss = 0.894235 (42.2 examples/sec)\
=> 2018-12-17 02:47:16.599457: step 6300, loss = 0.670258 (42.4 examples/sec)\
=> 2018-12-17 02:48:31.726464: step 6400, loss = 0.894856 (42.6 examples/sec)\
=> 2018-12-17 02:49:47.267544: step 6500, loss = 0.501398 (42.4 examples/sec)\
=> 2018-12-17 02:51:02.821311: step 6600, loss = 0.488761 (42.4 examples/sec)\
=> 2018-12-17 02:52:18.235816: step 6700, loss = 0.314195 (42.4 examples/sec)\
=> 2018-12-17 02:53:33.580118: step 6800, loss = 0.368690 (42.5 examples/sec)\
=> 2018-12-17 02:54:49.038008: step 6900, loss = 0.515403 (42.4 examples/sec)\
=> 2018-12-17 02:56:04.302243: step 7000, loss = 0.406949 (42.5 examples/sec)\
==> accuracy = 0.863133, best accuracy 0.855870\
=> 2018-12-17 02:59:27.753757: step 7100, loss = 0.998716 (42.2 examples/sec)\
=> 2018-12-17 03:00:43.748921: step 7200, loss = 0.316845 (42.1 examples/sec)\
=> 2018-12-17 03:01:59.907928: step 7300, loss = 1.907633 (42.0 examples/sec)\
=> 2018-12-17 03:03:16.097519: step 7400, loss = 0.829172 (42.0 examples/sec)\
=> 2018-12-17 03:04:32.160705: step 7500, loss = 0.889859 (42.1 examples/sec)\
=> 2018-12-17 03:05:47.983724: step 7600, loss = 0.450359 (42.2 examples/sec)\
=> 2018-12-17 03:07:03.957533: step 7700, loss = 0.772620 (42.1 examples/sec)\
=> 2018-12-17 03:08:19.624505: step 7800, loss = 1.100922 (42.3 examples/sec)\
=> 2018-12-17 03:09:35.672651: step 7900, loss = 0.545053 (42.1 examples/sec)\
=> 2018-12-17 03:10:51.650519: step 8000, loss = 2.439040 (42.1 examples/sec)\
==> accuracy = 0.877280, best accuracy 0.863133\
=> 2018-12-17 03:14:16.463714: step 8100, loss = 0.306034 (41.8 examples/sec)\
=> 2018-12-17 03:15:32.711064: step 8200, loss = 0.798734 (42.0 examples/sec)\
=> 2018-12-17 03:16:48.916759: step 8300, loss = 0.615459 (42.0 examples/sec)\
=> 2018-12-17 03:18:05.095905: step 8400, loss = 0.926586 (42.0 examples/sec)\
=> 2018-12-17 03:19:21.282070: step 8500, loss = 1.551592 (42.0 examples/sec)\
=> 2018-12-17 03:20:37.548572: step 8600, loss = 0.236412 (42.0 examples/sec)\
=> 2018-12-17 03:21:53.805678: step 8700, loss = 0.203472 (42.0 examples/sec)\
=> 2018-12-17 03:23:10.444143: step 8800, loss = 0.363312 (41.8 examples/sec)\
=> 2018-12-17 03:24:26.639337: step 8900, loss = 0.326578 (42.0 examples/sec)\
=> 2018-12-17 03:25:43.206282: step 9000, loss = 0.142586 (41.8 examples/sec)\
==> accuracy = 0.879730, best accuracy 0.877280\
=> 2018-12-17 03:29:07.954122: step 9100, loss = 0.423252 (42.1 examples/sec)\
=> 2018-12-17 03:30:24.038873: step 9200, loss = 1.081929 (42.1 examples/sec)\
=> 2018-12-17 03:31:40.181090: step 9300, loss = 0.715184 (42.0 examples/sec)\
=> 2018-12-17 03:32:56.897095: step 9400, loss = 0.405464 (41.7 examples/sec)\
=> 2018-12-17 03:34:13.653739: step 9500, loss = 0.215604 (41.7 examples/sec)\
=> 2018-12-17 03:35:30.484369: step 9600, loss = 0.625904 (41.7 examples/sec)\
=> 2018-12-17 03:36:47.526545: step 9700, loss = 0.440704 (41.5 examples/sec)\
=> 2018-12-17 03:38:04.301160: step 9800, loss = 0.425113 (41.7 examples/sec)\
=> 2018-12-17 03:39:20.970724: step 9900, loss = 0.361367 (41.7 examples/sec)\
=> 2018-12-17 03:40:38.097377: step 10000, loss = 0.386481 (41.5 examples/sec)\
==> accuracy = 0.888851, best accuracy 0.879730\
=> 2018-12-17 03:44:03.353726: step 10100, loss = 0.435677 (41.8 examples/sec)\
=> 2018-12-17 03:45:20.300903: step 10200, loss = 1.332121 (41.6 examples/sec)\
=> 2018-12-17 03:46:37.012573: step 10300, loss = 0.584493 (41.7 examples/sec)\
=> 2018-12-17 03:47:53.644006: step 10400, loss = 0.255574 (41.8 examples/sec)\
=> 2018-12-17 03:49:10.120544: step 10500, loss = 0.228146 (41.8 examples/sec)\
=> 2018-12-17 03:50:26.870687: step 10600, loss = 0.695827 (41.7 examples/sec)\
=> 2018-12-17 03:51:43.352238: step 10700, loss = 0.439331 (41.8 examples/sec)\
=> 2018-12-17 03:52:59.727919: step 10800, loss = 0.757444 (41.9 examples/sec)\
=> 2018-12-17 03:54:16.039054: step 10900, loss = 0.390478 (41.9 examples/sec)\
=> 2018-12-17 03:55:32.242329: step 11000, loss = 0.587768 (42.0 examples/sec)\
==> accuracy = 0.898944, best accuracy 0.888851\
=> 2018-12-17 03:58:56.359857: step 11100, loss = 0.194612 (41.9 examples/sec)\
=> 2018-12-17 04:00:12.416025: step 11200, loss = 0.440510 (42.1 examples/sec)\
=> 2018-12-17 04:01:28.165739: step 11300, loss = 0.844214 (42.2 examples/sec)\
=> 2018-12-17 04:02:44.029860: step 11400, loss = 1.143311 (42.2 examples/sec)\
=> 2018-12-17 04:04:00.128587: step 11500, loss = 1.023004 (42.1 examples/sec)\
=> 2018-12-17 04:05:16.393128: step 11600, loss = 0.558123 (42.0 examples/sec)\
=> 2018-12-17 04:06:32.557854: step 11700, loss = 0.222542 (42.0 examples/sec)\
=> 2018-12-17 04:07:48.629985: step 11800, loss = 0.356259 (42.1 examples/sec)\
=> 2018-12-17 04:09:04.918365: step 11900, loss = 1.167995 (41.9 examples/sec)\
=> 2018-12-17 04:10:21.004071: step 12000, loss = 0.868574 (42.1 examples/sec)\
==> accuracy = 0.903632, best accuracy 0.898944\
=> 2018-12-17 04:13:44.285681: step 12100, loss = 1.055987 (42.1 examples/sec)\
=> 2018-12-17 04:15:00.129826: step 12200, loss = 0.498828 (42.2 examples/sec)\
=> 2018-12-17 04:16:16.411868: step 12300, loss = 0.237248 (42.0 examples/sec)\
=> 2018-12-17 04:17:32.461624: step 12400, loss = 0.384566 (42.1 examples/sec)\
=> 2018-12-17 04:18:48.558961: step 12500, loss = 1.158343 (42.1 examples/sec)\
=> 2018-12-17 04:20:04.838136: step 12600, loss = 0.890094 (42.0 examples/sec)\
=> 2018-12-17 04:21:20.929167: step 12700, loss = 0.727219 (42.1 examples/sec)\
=> 2018-12-17 04:22:37.062436: step 12800, loss = 0.961422 (42.0 examples/sec)\
=> 2018-12-17 04:23:52.983924: step 12900, loss = 0.162201 (42.2 examples/sec)\
=> 2018-12-17 04:25:09.262006: step 13000, loss = 0.495103 (42.0 examples/sec)\
==> accuracy = 0.908573, best accuracy 0.903632\
=> 2018-12-17 04:28:32.954593: step 13100, loss = 0.334175 (42.0 examples/sec)\
=> 2018-12-17 04:29:49.358176: step 13200, loss = 0.865788 (41.9 examples/sec)\
=> 2018-12-17 04:31:05.561384: step 13300, loss = 0.152738 (42.0 examples/sec)\
=> 2018-12-17 04:32:21.516345: step 13400, loss = 0.145906 (42.1 examples/sec)\
=> 2018-12-17 04:33:37.691694: step 13500, loss = 0.197930 (42.0 examples/sec)\
=> 2018-12-17 04:34:54.530121: step 13600, loss = 0.286054 (41.6 examples/sec)\
=> 2018-12-17 04:36:11.291874: step 13700, loss = 0.598688 (41.7 examples/sec)\
=> 2018-12-17 04:37:27.413052: step 13800, loss = 0.644146 (42.0 examples/sec)\
=> 2018-12-17 04:38:43.663497: step 13900, loss = 0.343688 (42.0 examples/sec)\
=> 2018-12-17 04:40:00.045482: step 14000, loss = 0.550119 (41.9 examples/sec)\
==> accuracy = 0.906461, best accuracy 0.908573\
=> 2018-12-17 04:43:22.768770: step 14100, loss = 0.879578 (42.3 examples/sec)\
=> 2018-12-17 04:44:38.994914: step 14200, loss = 0.150192 (42.0 examples/sec)\
=> 2018-12-17 04:45:55.181956: step 14300, loss = 2.281345 (42.0 examples/sec)\
=> 2018-12-17 04:47:11.307347: step 14400, loss = 0.676499 (42.0 examples/sec)\
=> 2018-12-17 04:48:27.338015: step 14500, loss = 0.386503 (42.1 examples/sec)\
=> 2018-12-17 04:49:43.179830: step 14600, loss = 0.334067 (42.2 examples/sec)\
=> 2018-12-17 04:50:59.559970: step 14700, loss = 0.414763 (41.9 examples/sec)\
=> 2018-12-17 04:52:15.459448: step 14800, loss = 0.701905 (42.2 examples/sec)\
=> 2018-12-17 04:53:31.284392: step 14900, loss = 0.119933 (42.2 examples/sec)\
=> 2018-12-17 04:54:47.353844: step 15000, loss = 0.603379 (42.1 examples/sec)\
==> accuracy = 0.911909, best accuracy 0.908573\
=> 2018-12-17 04:58:10.859228: step 15100, loss = 0.424639 (42.1 examples/sec)\
=> 2018-12-17 04:59:26.706829: step 15200, loss = 0.191727 (42.2 examples/sec)\
=> 2018-12-17 05:00:42.948834: step 15300, loss = 0.304538 (42.0 examples/sec)\
=> 2018-12-17 05:01:59.454979: step 15400, loss = 0.216920 (41.8 examples/sec)\
=> 2018-12-17 05:03:15.160808: step 15500, loss = 0.166612 (42.3 examples/sec)\
=> 2018-12-17 05:04:31.089432: step 15600, loss = 0.068129 (42.1 examples/sec)\
=> 2018-12-17 05:05:47.329759: step 15700, loss = 0.373527 (42.0 examples/sec)\
=> 2018-12-17 05:07:03.216312: step 15800, loss = 0.540875 (42.2 examples/sec)\
=> 2018-12-17 05:08:19.080573: step 15900, loss = 0.333712 (42.2 examples/sec)\
=> 2018-12-17 05:09:35.008814: step 16000, loss = 0.352038 (42.1 examples/sec)\
==> accuracy = 0.913429, best accuracy 0.911909\
=> 2018-12-17 05:12:58.567243: step 16100, loss = 0.256829 (42.1 examples/sec)\
=> 2018-12-17 05:14:14.474142: step 16200, loss = 0.364653 (42.2 examples/sec)\
=> 2018-12-17 05:15:30.518715: step 16300, loss = 0.150577 (42.1 examples/sec)\
=> 2018-12-17 05:16:47.120368: step 16400, loss = 0.547013 (41.8 examples/sec)\
=> 2018-12-17 05:18:03.276170: step 16500, loss = 0.172790 (42.0 examples/sec)\
=> 2018-12-17 05:19:19.323772: step 16600, loss = 0.602443 (42.1 examples/sec)\
=> 2018-12-17 05:20:35.230124: step 16700, loss = 0.525583 (42.2 examples/sec)\
=> 2018-12-17 05:21:51.435362: step 16800, loss = 0.030193 (42.0 examples/sec)\
=> 2018-12-17 05:23:07.472616: step 16900, loss = 0.425497 (42.1 examples/sec)\
=> 2018-12-17 05:24:23.440775: step 17000, loss = 0.320927 (42.1 examples/sec)\
==> accuracy = 0.916723, best accuracy 0.913429\
=> Model saved to file: ./logs/train/model.ckpt-17000"

model_text_2="\
2018-12-17 04:42:19.766488: step 100, loss = 7.374277 (35.1 examples/sec)\
=> 2018-12-17 04:43:36.626446: step 200, loss = 7.622951 (41.6 examples/sec)\
=> 2018-12-17 04:44:53.768091: step 300, loss = 6.854950 (41.5 examples/sec)\
=> 2018-12-17 04:46:10.736669: step 400, loss = 5.969621 (41.6 examples/sec)\
=> 2018-12-17 04:47:27.970293: step 500, loss = 6.891289 (41.4 examples/sec)\
=> 2018-12-17 04:48:45.346153: step 600, loss = 6.281898 (41.4 examples/sec)\
=> 2018-12-17 04:50:02.800817: step 700, loss = 5.878906 (41.3 examples/sec)\
=> 2018-12-17 04:51:20.274677: step 800, loss = 6.522246 (41.3 examples/sec)\
=> 2018-12-17 04:52:38.149626: step 900, loss = 5.986090 (41.1 examples/sec)\
=> 2018-12-17 04:53:55.817784: step 1000, loss = 5.698441 (41.2 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.019998, best accuracy 0.000000\
=> Model saved to file: ./logs/train/model.ckpt-1000\
=> patience = 100\
=> 2018-12-17 04:57:24.940787: step 1100, loss = 6.045772 (40.8 examples/sec)\
=> 2018-12-17 04:58:43.400679: step 1200, loss = 5.523099 (40.8 examples/sec)\
=> 2018-12-17 05:00:02.201234: step 1300, loss = 4.815417 (40.6 examples/sec)\
=> 2018-12-17 05:01:20.802684: step 1400, loss = 5.102162 (40.7 examples/sec)\
=> 2018-12-17 05:02:38.364283: step 1500, loss = 4.947105 (41.3 examples/sec)\
=> 2018-12-17 05:03:56.222933: step 1600, loss = 4.796908 (41.1 examples/sec)\
=> 2018-12-17 05:05:13.649235: step 1700, loss = 3.719654 (41.3 examples/sec)\
=> 2018-12-17 05:06:31.378112: step 1800, loss = 4.039759 (41.2 examples/sec)\
=> 2018-12-17 05:07:48.998160: step 1900, loss = 3.314461 (41.2 examples/sec)\
=> 2018-12-17 05:09:06.483726: step 2000, loss = 3.974345 (41.3 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.305197, best accuracy 0.019998\
=> Model saved to file: ./logs/train/model.ckpt-2000\
=> patience = 100\
=> 2018-12-17 05:12:33.950176: step 2100, loss = 3.126018 (41.4 examples/sec)\
=> 2018-12-17 05:13:51.505396: step 2200, loss = 2.152705 (41.3 examples/sec)\
=> 2018-12-17 05:15:09.331787: step 2300, loss = 3.255496 (41.1 examples/sec)\
=> 2018-12-17 05:16:27.358743: step 2400, loss = 2.143888 (41.0 examples/sec)\
=> 2018-12-17 05:17:45.763265: step 2500, loss = 2.113324 (40.8 examples/sec)\
=> 2018-12-17 05:19:03.504174: step 2600, loss = 1.253796 (41.2 examples/sec)\
=> 2018-12-17 05:20:21.500153: step 2700, loss = 1.945674 (41.0 examples/sec)\
=> 2018-12-17 05:21:39.535118: step 2800, loss = 1.244949 (41.0 examples/sec)\
=> 2018-12-17 05:22:57.031927: step 2900, loss = 2.133479 (41.3 examples/sec)\
=> 2018-12-17 05:24:14.309627: step 3000, loss = 2.061948 (41.4 examples/sec)\
==> accuracy = 0.630520, best accuracy 0.305197\
=> 2018-12-17 05:27:41.185919: step 3100, loss = 1.760384 (41.5 examples/sec)\
=> 2018-12-17 05:28:58.128009: step 3200, loss = 2.436023 (41.6 examples/sec)\
=> 2018-12-17 05:30:15.297930: step 3300, loss = 1.362783 (41.5 examples/sec)\
=> 2018-12-17 05:31:32.345720: step 3400, loss = 1.790114 (41.5 examples/sec)\
=> 2018-12-17 05:32:49.152886: step 3500, loss = 1.371933 (41.7 examples/sec)\
=> 2018-12-17 05:34:06.354512: step 3600, loss = 0.946622 (41.5 examples/sec)\
=> 2018-12-17 05:35:23.959036: step 3700, loss = 0.795298 (41.2 examples/sec)\
=> 2018-12-17 05:36:41.490282: step 3800, loss = 1.489907 (41.3 examples/sec)\
=> 2018-12-17 05:37:58.199459: step 3900, loss = 1.782596 (41.7 examples/sec)\
=> 2018-12-17 05:39:15.683980: step 4000, loss = 1.113226 (41.3 examples/sec)\
==> accuracy = 0.730129, best accuracy 0.630520\
=> 2018-12-17 05:42:42.280339: step 4100, loss = 1.651828 (41.5 examples/sec)\
=> 2018-12-17 05:43:59.190230: step 4200, loss = 1.417409 (41.6 examples/sec)\
=> 2018-12-17 05:45:16.466058: step 4300, loss = 1.212518 (41.4 examples/sec)\
=> 2018-12-17 05:46:34.709953: step 4400, loss = 1.312670 (40.9 examples/sec)\
=> 2018-12-17 05:47:52.075918: step 4500, loss = 0.783423 (41.4 examples/sec)\
=> 2018-12-17 05:49:08.823631: step 4600, loss = 1.641372 (41.7 examples/sec)\
=> 2018-12-17 05:50:25.697266: step 4700, loss = 2.075889 (41.6 examples/sec)\
=> 2018-12-17 05:51:42.473123: step 4800, loss = 1.457590 (41.7 examples/sec)\
=> 2018-12-17 05:52:59.989360: step 4900, loss = 1.685263 (41.3 examples/sec)\
=> 2018-12-17 05:54:17.554517: step 5000, loss = 0.922981 (41.3 examples/sec)\
==> accuracy = 0.794073, best accuracy 0.730129\
=> 2018-12-17 05:57:44.143694: step 5100, loss = 0.713665 (41.4 examples/sec)\
=> 2018-12-17 05:59:01.857434: step 5200, loss = 0.845487 (41.2 examples/sec)\
=> 2018-12-17 06:00:20.343734: step 5300, loss = 1.856222 (40.8 examples/sec)\
=> 2018-12-17 06:01:37.941384: step 5400, loss = 1.268394 (41.2 examples/sec)\
=> 2018-12-17 06:02:55.780600: step 5500, loss = 1.090100 (41.1 examples/sec)\
=> 2018-12-17 06:04:13.798057: step 5600, loss = 0.621115 (41.0 examples/sec)\
=> 2018-12-17 06:05:32.184943: step 5700, loss = 1.334868 (40.8 examples/sec)\
=> 2018-12-17 06:06:50.232319: step 5800, loss = 1.121701 (41.0 examples/sec)\
=> 2018-12-17 06:08:07.795906: step 5900, loss = 0.966653 (41.3 examples/sec)\
=> 2018-12-17 06:09:25.342311: step 6000, loss = 0.638292 (41.3 examples/sec)\
==> accuracy = 0.831564, best accuracy 0.794073\
=> 2018-12-17 06:12:52.325292: step 6100, loss = 1.954429 (41.2 examples/sec)\
=> 2018-12-17 06:14:09.971241: step 6200, loss = 1.134073 (41.2 examples/sec)\
=> 2018-12-17 06:15:27.332691: step 6300, loss = 1.876579 (41.4 examples/sec)\
=> 2018-12-17 06:16:45.125280: step 6400, loss = 1.048157 (41.1 examples/sec)\
=> 2018-12-17 06:18:02.735042: step 6500, loss = 1.164920 (41.2 examples/sec)\
=> 2018-12-17 06:19:20.956001: step 6600, loss = 1.061879 (40.9 examples/sec)\
=> 2018-12-17 06:20:38.658906: step 6700, loss = 3.208707 (41.2 examples/sec)\
=> 2018-12-17 06:21:56.058732: step 6800, loss = 0.624459 (41.3 examples/sec)\
=> 2018-12-17 06:23:13.441583: step 6900, loss = 0.691778 (41.4 examples/sec)\
=> 2018-12-17 06:24:30.967644: step 7000, loss = 1.396799 (41.3 examples/sec)\
==> accuracy = 0.843283, best accuracy 0.831564\
=> 2018-12-17 06:27:59.181229: step 7100, loss = 1.974226 (41.1 examples/sec)\
=> 2018-12-17 06:29:16.858941: step 7200, loss = 0.415440 (41.2 examples/sec)\
=> 2018-12-17 06:30:33.912055: step 7300, loss = 1.822256 (41.5 examples/sec)\
=> 2018-12-17 06:31:50.980036: step 7400, loss = 0.838417 (41.5 examples/sec)\
=> 2018-12-17 06:33:08.409148: step 7500, loss = 0.791687 (41.3 examples/sec)\
=> 2018-12-17 06:34:25.673264: step 7600, loss = 0.845440 (41.4 examples/sec)\
=> 2018-12-17 06:35:42.601126: step 7700, loss = 0.605120 (41.6 examples/sec)\
=> 2018-12-17 06:36:59.770692: step 7800, loss = 0.391207 (41.5 examples/sec)\
=> 2018-12-17 06:38:16.986604: step 7900, loss = 0.379844 (41.4 examples/sec)\
=> 2018-12-17 06:39:35.224873: step 8000, loss = 0.806030 (40.9 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.835470, best accuracy 0.843283\
=> patience = 99\
=> 2018-12-17 06:43:01.944629: step 8100, loss = 2.420620 (41.2 examples/sec)\
=> 2018-12-17 06:44:19.495344: step 8200, loss = 0.651898 (41.3 examples/sec)\
=> 2018-12-17 06:45:36.706183: step 8300, loss = 0.461119 (41.4 examples/sec)\
=> 2018-12-17 06:46:53.723046: step 8400, loss = 0.476671 (41.6 examples/sec)\
=> 2018-12-17 06:48:10.944396: step 8500, loss = 0.566017 (41.4 examples/sec)\
=> 2018-12-17 06:49:28.693793: step 8600, loss = 0.793647 (41.2 examples/sec)\
=> 2018-12-17 06:50:45.551479: step 8700, loss = 0.649750 (41.6 examples/sec)\
=> 2018-12-17 06:52:02.359659: step 8800, loss = 0.388437 (41.7 examples/sec)\
=> 2018-12-17 06:53:19.363567: step 8900, loss = 0.269785 (41.6 examples/sec)\
=> 2018-12-17 06:54:36.631897: step 9000, loss = 1.577913 (41.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.842094, best accuracy 0.843283\
=> patience = 98\
=> 2018-12-17 06:58:02.050066: step 9100, loss = 1.136587 (41.6 examples/sec)\
=> 2018-12-17 06:59:18.971286: step 9200, loss = 0.420158 (41.6 examples/sec)\
=> 2018-12-17 07:00:35.413362: step 9300, loss = 1.293398 (41.9 examples/sec)\
=> 2018-12-17 07:01:51.895438: step 9400, loss = 0.810112 (41.8 examples/sec)\
=> 2018-12-17 07:03:08.561110: step 9500, loss = 0.578729 (41.7 examples/sec)\
=> 2018-12-17 07:04:25.550928: step 9600, loss = 0.545799 (41.6 examples/sec)\
=> 2018-12-17 07:05:42.111300: step 9700, loss = 0.522498 (41.8 examples/sec)\
=> 2018-12-17 07:06:58.505331: step 9800, loss = 0.514425 (41.9 examples/sec)\
=> 2018-12-17 07:08:15.486768: step 9900, loss = 0.343015 (41.6 examples/sec)\
=> 2018-12-17 07:09:32.863596: step 10000, loss = 0.284787 (41.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.869268, best accuracy 0.843283\
=> Model saved to file: ./logs/train/model.ckpt-10000\
=> patience = 100\
=> 2018-12-17 07:12:59.052297: step 10100, loss = 1.171155 (41.5 examples/sec)\
=> 2018-12-17 07:14:15.923283: step 10200, loss = 0.727466 (41.6 examples/sec)\
=> 2018-12-17 07:15:32.879135: step 10300, loss = 0.261393 (41.6 examples/sec)\
=> 2018-12-17 07:16:49.203841: step 10400, loss = 0.481196 (41.9 examples/sec)\
=> 2018-12-17 07:18:05.893846: step 10500, loss = 0.407274 (41.7 examples/sec)\
=> 2018-12-17 07:19:22.777906: step 10600, loss = 0.983259 (41.6 examples/sec)\
=> 2018-12-17 07:20:40.057593: step 10700, loss = 0.781765 (41.4 examples/sec)\
=> 2018-12-17 07:21:56.851453: step 10800, loss = 0.960308 (41.7 examples/sec)\
=> 2018-12-17 07:23:13.755089: step 10900, loss = 1.771203 (41.6 examples/sec)\
=> 2018-12-17 07:24:30.273367: step 11000, loss = 0.885539 (41.8 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.881242, best accuracy 0.869268\
=> Model saved to file: ./logs/train/model.ckpt-11000\
=> patience = 100\
=> 2018-12-17 07:27:55.441798: step 11100, loss = 0.493309 (41.9 examples/sec)\
=> 2018-12-17 07:29:12.081425: step 11200, loss = 0.294098 (41.8 examples/sec)\
=> 2018-12-17 07:30:29.140036: step 11300, loss = 0.313843 (41.5 examples/sec)\
=> 2018-12-17 07:31:46.057361: step 11400, loss = 1.003654 (41.6 examples/sec)\
=> 2018-12-17 07:33:03.110383: step 11500, loss = 0.690264 (41.5 examples/sec)\
=> 2018-12-17 07:34:20.214954: step 11600, loss = 1.130753 (41.5 examples/sec)\
=> 2018-12-17 07:35:37.534449: step 11700, loss = 0.354808 (41.4 examples/sec)\
=> 2018-12-17 07:36:54.270713: step 11800, loss = 0.779385 (41.7 examples/sec)\
=> 2018-12-17 07:38:10.692407: step 11900, loss = 0.277697 (41.9 examples/sec)\
=> 2018-12-17 07:39:27.352397: step 12000, loss = 0.924470 (41.7 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.896824, best accuracy 0.881242\
=> Model saved to file: ./logs/train/model.ckpt-12000\
=> patience = 100\
=> 2018-12-17 07:42:52.702343: step 12100, loss = 0.418763 (41.8 examples/sec)\
=> 2018-12-17 07:44:09.085529: step 12200, loss = 0.491518 (41.9 examples/sec)\
=> 2018-12-17 07:45:25.342084: step 12300, loss = 0.199402 (42.0 examples/sec)\
=> 2018-12-17 07:46:42.200450: step 12400, loss = 0.509919 (41.6 examples/sec)\
=> 2018-12-17 07:47:58.368689: step 12500, loss = 1.302066 (42.0 examples/sec)\
=> 2018-12-17 07:49:14.586133: step 12600, loss = 0.800572 (42.0 examples/sec)\
=> 2018-12-17 07:50:30.825450: step 12700, loss = 0.253908 (42.0 examples/sec)\
=> 2018-12-17 07:51:47.693023: step 12800, loss = 0.326790 (41.6 examples/sec)\
=> 2018-12-17 07:53:04.366565: step 12900, loss = 0.503465 (41.7 examples/sec)\
=> 2018-12-17 07:54:21.172421: step 13000, loss = 0.587188 (41.7 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.896824, best accuracy 0.896824\
=> patience = 99\
=> 2018-12-17 07:57:45.522922: step 13100, loss = 0.958774 (42.0 examples/sec)\
=> 2018-12-17 07:59:02.004047: step 13200, loss = 0.702744 (41.8 examples/sec)\
=> 2018-12-17 08:00:18.078426: step 13300, loss = 0.817832 (42.1 examples/sec)\
=> 2018-12-17 08:01:34.594887: step 13400, loss = 0.400130 (41.8 examples/sec)\
=> 2018-12-17 08:02:50.620308: step 13500, loss = 0.349182 (42.1 examples/sec)\
=> 2018-12-17 08:04:06.930932: step 13600, loss = 0.549410 (41.9 examples/sec)\
=> 2018-12-17 08:05:23.213957: step 13700, loss = 0.669667 (42.0 examples/sec)\
=> 2018-12-17 08:06:39.799947: step 13800, loss = 1.007925 (41.8 examples/sec)\
=> 2018-12-17 08:07:56.073603: step 13900, loss = 0.308014 (42.0 examples/sec)\
=> 2018-12-17 08:09:12.440631: step 14000, loss = 0.113805 (41.9 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.897036, best accuracy 0.896824\
=> Model saved to file: ./logs/train/model.ckpt-14000\
=> patience = 100\
=> 2018-12-17 08:12:37.950408: step 14100, loss = 0.212590 (41.5 examples/sec)\
=> 2018-12-17 08:13:54.889848: step 14200, loss = 0.418393 (41.6 examples/sec)\
=> 2018-12-17 08:15:11.570024: step 14300, loss = 0.146582 (41.7 examples/sec)\
=> 2018-12-17 08:16:28.371960: step 14400, loss = 1.269759 (41.7 examples/sec)\
=> 2018-12-17 08:17:45.146838: step 14500, loss = 0.595010 (41.7 examples/sec)\
=> 2018-12-17 08:19:02.079578: step 14600, loss = 0.358445 (41.6 examples/sec)\
=> 2018-12-17 08:20:18.443623: step 14700, loss = 0.222201 (41.9 examples/sec)\
=> 2018-12-17 08:21:34.785162: step 14800, loss = 0.051814 (41.9 examples/sec)\
=> 2018-12-17 08:22:52.113638: step 14900, loss = 0.924230 (41.4 examples/sec)\
=> 2018-12-17 08:24:08.980362: step 15000, loss = 1.145403 (41.6 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.903915, best accuracy 0.897036\
=> Model saved to file: ./logs/train/model.ckpt-15000\
=> patience = 100\
=> 2018-12-17 08:27:35.249538: step 15100, loss = 1.256847 (41.3 examples/sec)\
=> 2018-12-17 08:28:52.354733: step 15200, loss = 0.125334 (41.5 examples/sec)\
=> 2018-12-17 08:30:09.606865: step 15300, loss = 0.145317 (41.4 examples/sec)\
=> 2018-12-17 08:31:26.505771: step 15400, loss = 0.262285 (41.6 examples/sec)\
=> 2018-12-17 08:32:43.695808: step 15500, loss = 0.061056 (41.5 examples/sec)\
=> 2018-12-17 08:34:00.554238: step 15600, loss = 1.051494 (41.6 examples/sec)\
=> 2018-12-17 08:35:17.869519: step 15700, loss = 0.353310 (41.4 examples/sec)\
=> 2018-12-17 08:36:34.704945: step 15800, loss = 0.693863 (41.6 examples/sec)\
=> 2018-12-17 08:37:52.103757: step 15900, loss = 0.263498 (41.3 examples/sec)\
=> 2018-12-17 08:39:08.946066: step 16000, loss = 0.519905 (41.6 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.905443, best accuracy 0.903915\
=> Model saved to file: ./logs/train/model.ckpt-16000\
=> patience = 100\
=> 2018-12-17 08:42:35.315867: step 16100, loss = 0.097198 (41.5 examples/sec)\
=> 2018-12-17 08:43:52.049231: step 16200, loss = 0.181992 (41.7 examples/sec)\
=> 2018-12-17 08:45:09.448586: step 16300, loss = 0.203313 (41.3 examples/sec)\
=> 2018-12-17 08:46:26.139698: step 16400, loss = 0.163585 (41.7 examples/sec)\
=> 2018-12-17 08:47:43.176360: step 16500, loss = 0.557078 (41.5 examples/sec)\
=> 2018-12-17 08:48:59.657094: step 16600, loss = 0.959278 (41.8 examples/sec)\
=> 2018-12-17 08:50:16.775350: step 16700, loss = 0.475545 (41.5 examples/sec)\
=> 2018-12-17 08:51:33.458283: step 16800, loss = 0.902802 (41.7 examples/sec)\
=> 2018-12-17 08:52:50.578920: step 16900, loss = 0.647487 (41.5 examples/sec)\
=> 2018-12-17 08:54:07.387468: step 17000, loss = 0.094052 (41.7 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.912449, best accuracy 0.905443\
=> Model saved to file: ./logs/train/model.ckpt-17000\
"
model_text_3="\
> 2018-12-17 03:36:03.773373: step 100, loss = 7.825383 (57.1 examples/sec)\
=> 2018-12-17 03:36:45.682289: step 200, loss = 6.926432 (76.4 examples/sec)\
=> 2018-12-17 03:37:27.591562: step 300, loss = 6.937031 (76.4 examples/sec)\
=> 2018-12-17 03:38:09.372735: step 400, loss = 6.529932 (76.6 examples/sec)\
=> 2018-12-17 03:38:51.028165: step 500, loss = 6.431801 (76.8 examples/sec)\
=> 2018-12-17 03:39:32.636596: step 600, loss = 6.235023 (76.9 examples/sec)\
=> 2018-12-17 03:40:14.210166: step 700, loss = 6.674021 (77.0 examples/sec)\
=> 2018-12-17 03:40:55.694617: step 800, loss = 7.183585 (77.1 examples/sec)\
=> 2018-12-17 03:41:37.246743: step 900, loss = 6.842922 (77.0 examples/sec)\
=> 2018-12-17 03:42:18.705473: step 1000, loss = 6.081688 (77.2 examples/sec)\
==> accuracy = 0.043478, best accuracy 0.000000\
=> 2018-12-17 03:44:27.666063: step 1100, loss = 5.338964 (77.2 examples/sec)\
=> 2018-12-17 03:45:09.155590: step 1200, loss = 6.350661 (77.1 examples/sec)\
=> 2018-12-17 03:45:50.820596: step 1300, loss = 4.947772 (76.8 examples/sec)\
=> 2018-12-17 03:46:32.420997: step 1400, loss = 5.007609 (76.9 examples/sec)\
=> 2018-12-17 03:47:13.939046: step 1500, loss = 5.467885 (77.1 examples/sec)\
=> 2018-12-17 03:47:55.503809: step 1600, loss = 4.120806 (77.0 examples/sec)\
=> 2018-12-17 03:48:37.107324: step 1700, loss = 3.538748 (76.9 examples/sec)\
=> 2018-12-17 03:49:18.764497: step 1800, loss = 3.918617 (76.8 examples/sec)\
=> 2018-12-17 03:50:00.399877: step 1900, loss = 3.010329 (76.9 examples/sec)\
=> 2018-12-17 03:50:42.023874: step 2000, loss = 3.859855 (76.9 examples/sec)\
==> accuracy = 0.367357, best accuracy 0.043478\
52:51.656599: step 2100, loss = 2.743831 (76.7 examples/sec)\
=> 2018-12-17 03:53:33.357894: step 2200, loss = 3.615383 (76.7 examples/sec)\
=> 2018-12-17 03:54:14.971896: step 2300, loss = 3.189612 (76.9 examples/sec)\
=> 2018-12-17 03:54:56.505414: step 2400, loss = 3.329175 (77.1 examples/sec)\
=> 2018-12-17 03:55:37.975633: step 2500, loss = 3.259444 (77.2 examples/sec)\
=> 2018-12-17 03:56:19.682465: step 2600, loss = 2.529315 (76.7 examples/sec)\
=> 2018-12-17 03:57:01.427062: step 2700, loss = 2.040850 (76.7 examples/sec)\
=> 2018-12-17 03:57:43.116646: step 2800, loss = 1.861279 (76.8 examples/sec)\
=> 2018-12-17 03:58:24.776317: step 2900, loss = 1.732963 (76.8 examples/sec)\
=> 2018-12-17 03:59:06.492980: step 3000, loss = 1.179314 (76.7 examples/sec)\
==> accuracy = 0.620457, best accuracy 0.367357\
=> 2018-12-17 04:01:14.696229: step 3100, loss = 1.528957 (77.0 examples/sec)\
=> 2018-12-17 04:01:56.505712: step 3200, loss = 2.447804 (76.5 examples/sec)\
=> 2018-12-17 04:02:38.202943: step 3300, loss = 1.121612 (76.8 examples/sec)\
=> 2018-12-17 04:03:19.900783: step 3400, loss = 1.128439 (76.8 examples/sec)\
=> 2018-12-17 04:04:01.658681: step 3500, loss = 1.490637 (76.6 examples/sec)\
=> 2018-12-17 04:04:43.235611: step 3600, loss = 1.537704 (77.0 examples/sec)\
=> 2018-12-17 04:05:24.824828: step 3700, loss = 2.239595 (77.0 examples/sec)\
=> 2018-12-17 04:06:06.451992: step 3800, loss = 1.488783 (76.9 examples/sec)\
=> 2018-12-17 04:06:48.129682: step 3900, loss = 1.483115 (76.8 examples/sec)\
=> 2018-12-17 04:07:29.366343: step 4000, loss = 1.632385 (77.6 examples/sec)\
==> accuracy = 0.710895, best accuracy 0.620457\
=> 2018-12-17 04:09:38.115030: step 4100, loss = 0.910603 (77.3 examples/sec)\
=> 2018-12-17 04:10:19.545589: step 4200, loss = 2.012977 (77.2 examples/sec)\
=> 2018-12-17 04:11:00.909883: step 4300, loss = 0.787164 (77.4 examples/sec)\
=> 2018-12-17 04:11:42.428030: step 4400, loss = 1.144536 (77.1 examples/sec)\
=> 2018-12-17 04:12:23.798488: step 4500, loss = 2.382068 (77.4 examples/sec)\
=> 2018-12-17 04:13:04.995926: step 4600, loss = 2.580159 (77.7 examples/sec)\
=> 2018-12-17 04:13:46.239857: step 4700, loss = 1.680448 (77.6 examples/sec)\
=> 2018-12-17 04:14:27.482309: step 4800, loss = 1.614756 (77.6 examples/sec)\
=> 2018-12-17 04:15:08.716767: step 4900, loss = 1.133621 (77.6 examples/sec)\
=> 2018-12-17 04:15:50.121028: step 5000, loss = 0.816216 (77.3 examples/sec)\
==> accuracy = 0.771399, best accuracy 0.710895\
=> 2018-12-17 04:17:56.976171: step 5100, loss = 0.957452 (76.9 examples/sec)\
=> 2018-12-17 04:18:38.631406: step 5200, loss = 0.506637 (76.8 examples/sec)\
=> 2018-12-17 04:19:20.290225: step 5300, loss = 1.035684 (76.8 examples/sec)\
=> 2018-12-17 04:20:02.064063: step 5400, loss = 1.647039 (76.6 examples/sec)\
=> 2018-12-17 04:20:43.641065: step 5500, loss = 1.126728 (77.0 examples/sec)\
=> 2018-12-17 04:21:24.906731: step 5600, loss = 0.888875 (77.6 examples/sec)\
=> 2018-12-17 04:22:06.433264: step 5700, loss = 0.880704 (77.1 examples/sec)\
=> 2018-12-17 04:22:48.003858: step 5800, loss = 1.254857 (77.0 examples/sec)\
=> 2018-12-17 04:23:29.374718: step 5900, loss = 1.056074 (77.4 examples/sec)\
=> 2018-12-17 04:24:10.676534: step 6000, loss = 0.916247 (77.5 examples/sec)\
==> accuracy = 0.806004, best accuracy 0.771399\
=> 2018-12-17 04:26:17.004137: step 6100, loss = 0.801138 (77.4 examples/sec)\
=> 2018-12-17 04:26:58.477387: step 6200, loss = 0.922682 (77.2 examples/sec)\
=> 2018-12-17 04:27:39.782261: step 6300, loss = 1.188087 (77.5 examples/sec)\
=> 2018-12-17 04:28:21.239680: step 6400, loss = 1.260435 (77.2 examples/sec)\
=> 2018-12-17 04:29:02.624798: step 6500, loss = 1.109577 (77.3 examples/sec)\
=> 2018-12-17 04:29:44.048251: step 6600, loss = 1.445254 (77.3 examples/sec)\
=> 2018-12-17 04:30:25.373830: step 6700, loss = 0.776664 (77.4 examples/sec)\
=> 2018-12-17 04:31:06.436321: step 6800, loss = 1.482431 (77.9 examples/sec)\
=> 2018-12-17 04:31:47.449247: step 6900, loss = 0.602766 (78.0 examples/sec)\
=> 2018-12-17 04:32:28.811180: step 7000, loss = 0.647421 (77.4 examples/sec)\
==> accuracy = 0.821034, best accuracy 0.806004\
=> 2018-12-17 04:34:35.410765: step 7100, loss = 1.025157 (77.4 examples/sec)\
=> 2018-12-17 04:35:16.684101: step 7200, loss = 1.441535 (77.5 examples/sec)\
=> 2018-12-17 04:35:57.965229: step 7300, loss = 0.511033 (77.5 examples/sec)\
=> 2018-12-17 04:36:39.163237: step 7400, loss = 1.179535 (77.7 examples/sec)\
=> 2018-12-17 04:37:20.744326: step 7500, loss = 1.345289 (77.0 examples/sec)\
=> 2018-12-17 04:38:02.198745: step 7600, loss = 0.843720 (77.2 examples/sec)\
=> 2018-12-17 04:38:43.634832: step 7700, loss = 0.966955 (77.2 examples/sec)\
=> 2018-12-17 04:39:25.114356: step 7800, loss = 3.368572 (77.2 examples/sec)\
=> 2018-12-17 04:40:06.555562: step 7900, loss = 0.986243 (77.2 examples/sec)\
=> 2018-12-17 04:40:48.022543: step 8000, loss = 0.620610 (77.2 examples/sec)\
==> accuracy = 0.825153, best accuracy 0.821034\
=> 2018-12-17 04:42:54.998072: step 8100, loss = 0.864005 (77.1 examples/sec)\
=> 2018-12-17 04:43:36.432801: step 8200, loss = 0.488855 (77.2 examples/sec)\
=> 2018-12-17 04:44:17.923636: step 8300, loss = 0.492607 (77.1 examples/sec)\
=> 2018-12-17 04:44:59.339678: step 8400, loss = 1.780721 (77.3 examples/sec)\
=> 2018-12-17 04:45:40.484065: step 8500, loss = 0.383611 (77.8 examples/sec)\
=> 2018-12-17 04:46:21.619485: step 8600, loss = 0.565200 (77.8 examples/sec)\
=> 2018-12-17 04:47:02.820421: step 8700, loss = 0.612679 (77.7 examples/sec)\
=> 2018-12-17 04:47:44.291714: step 8800, loss = 1.076017 (77.2 examples/sec)\
=> 2018-12-17 04:48:25.370675: step 8900, loss = 1.537303 (77.9 examples/sec)\
=> 2018-12-17 04:49:06.681190: step 9000, loss = 0.478520 (77.5 examples/sec)\
==> accuracy = 0.855341, best accuracy 0.825153\
=> 2018-12-17 04:51:14.618755: step 9100, loss = 0.129899 (77.7 examples/sec)\
=> 2018-12-17 04:51:55.703248: step 9200, loss = 0.667702 (77.9 examples/sec)\
=> 2018-12-17 04:52:36.948726: step 9300, loss = 0.408826 (77.6 examples/sec)\
=> 2018-12-17 04:53:18.175897: step 9400, loss = 1.016215 (77.6 examples/sec)\
=> 2018-12-17 04:53:59.299444: step 9500, loss = 0.309090 (77.8 examples/sec)\
=> 2018-12-17 04:54:40.386631: step 9600, loss = 0.452641 (77.9 examples/sec)\
=> 2018-12-17 04:55:21.385545: step 9700, loss = 0.804083 (78.1 examples/sec)\
=> 2018-12-17 04:56:02.350317: step 9800, loss = 1.141823 (78.1 examples/sec)\
=> 2018-12-17 04:56:43.465138: step 9900, loss = 0.796880 (77.8 examples/sec)\
=> 2018-12-17 04:57:24.656742: step 10000, loss = 0.322560 (77.7 examples/sec)\
==> accuracy = 0.865489, best accuracy 0.855341\
=> 2018-12-17 05:03:47.768102: step 10100, loss = 0.616885 (56.0 examples/sec)\
=> 2018-12-17 05:04:29.293210: step 10200, loss = 0.956570 (77.1 examples/sec)\
=> 2018-12-17 05:05:10.826573: step 10300, loss = 0.562371 (77.1 examples/sec)\
=> 2018-12-17 05:05:52.324821: step 10400, loss = 0.768137 (77.1 examples/sec)\
=> 2018-12-17 05:06:33.656323: step 10500, loss = 0.499357 (77.4 examples/sec)\
=> 2018-12-17 05:07:14.948165: step 10600, loss = 0.679285 (77.5 examples/sec)\
=> 2018-12-17 05:07:56.516957: step 10700, loss = 0.469891 (77.0 examples/sec)\
=> 2018-12-17 05:08:38.257117: step 10800, loss = 0.476982 (76.7 examples/sec)\
=> 2018-12-17 05:09:19.849121: step 10900, loss = 0.246298 (76.9 examples/sec)\
=> 2018-12-17 05:10:01.380193: step 11000, loss = 1.041359 (77.1 examples/sec)\
==> accuracy = 0.871985, best accuracy 0.000000\
=> 2018-12-17 05:12:08.262912: step 11100, loss = 0.486148 (77.5 examples/sec)\
=> 2018-12-17 05:12:49.704068: step 11200, loss = 0.573467 (77.2 examples/sec)\
=> 2018-12-17 05:13:31.211745: step 11300, loss = 0.359518 (77.1 examples/sec)\
=> 2018-12-17 05:14:12.542145: step 11400, loss = 0.777549 (77.4 examples/sec)\
=> 2018-12-17 05:14:53.806727: step 11500, loss = 0.624774 (77.6 examples/sec)\
=> 2018-12-17 05:15:35.212143: step 11600, loss = 0.329052 (77.3 examples/sec)\
=> 2018-12-17 05:16:16.485248: step 11700, loss = 0.286304 (77.5 examples/sec)\
=> 2018-12-17 05:16:57.648706: step 11800, loss = 0.823731 (77.7 examples/sec)\
=> 2018-12-17 05:17:38.786989: step 11900, loss = 0.818910 (77.8 examples/sec)\
=> 2018-12-17 05:18:20.068107: step 12000, loss = 1.058540 (77.5 examples/sec)\
==> accuracy = 0.885360, best accuracy 0.871985\
=> 2018-12-17 05:20:29.514279: step 12100, loss = 1.083464 (77.2 examples/sec)\
=> 2018-12-17 05:21:10.899820: step 12200, loss = 0.335674 (77.3 examples/sec)\
=> 2018-12-17 05:21:52.240237: step 12300, loss = 0.419229 (77.4 examples/sec)\
=> 2018-12-17 05:22:33.564979: step 12400, loss = 0.791127 (77.4 examples/sec)\
=> 2018-12-17 05:23:14.803149: step 12500, loss = 0.309961 (77.6 examples/sec)\
=> 2018-12-17 05:23:56.222394: step 12600, loss = 0.557747 (77.3 examples/sec)\
=> 2018-12-17 05:24:37.586501: step 12700, loss = 0.381344 (77.4 examples/sec)\
=> 2018-12-17 05:25:18.824744: step 12800, loss = 0.514333 (77.6 examples/sec)\
=> 2018-12-17 05:26:00.045470: step 12900, loss = 0.832550 (77.6 examples/sec)\
=> 2018-12-17 05:26:41.387264: step 13000, loss = 0.156266 (77.4 examples/sec)\
==> accuracy = 0.881029, best accuracy 0.885360\
=> 2018-12-17 05:28:47.811421: step 13100, loss = 1.000100 (77.4 examples/sec)\
=> 2018-12-17 05:29:29.129239: step 13200, loss = 0.453818 (77.5 examples/sec)\
=> 2018-12-17 05:30:10.452888: step 13300, loss = 0.300923 (77.4 examples/sec)\
=> 2018-12-17 05:30:51.752809: step 13400, loss = 1.545806 (77.5 examples/sec)\
=> 2018-12-17 05:31:33.104718: step 13500, loss = 0.576512 (77.4 examples/sec)\
=> 2018-12-17 05:32:14.424760: step 13600, loss = 0.872062 (77.5 examples/sec)\
=> 2018-12-17 05:32:55.733707: step 13700, loss = 0.408503 (77.5 examples/sec)\
=> 2018-12-17 05:33:37.113015: step 13800, loss = 0.430812 (77.3 examples/sec)\
=> 2018-12-17 05:34:18.595838: step 13900, loss = 0.342744 (77.1 examples/sec)\
=> 2018-12-17 05:35:00.024333: step 14000, loss = 0.640258 (77.2 examples/sec)\
==> accuracy = 0.887398, best accuracy 0.885360\
=> 2018-12-17 05:37:08.838756: step 14100, loss = 0.645338 (77.5 examples/sec)\
=> 2018-12-17 05:37:50.193056: step 14200, loss = 0.271792 (77.4 examples/sec)\
=> 2018-12-17 05:38:31.622478: step 14300, loss = 0.268625 (77.2 examples/sec)\
=> 2018-12-17 05:39:13.082760: step 14400, loss = 0.379954 (77.2 examples/sec)\
=> 2018-12-17 05:39:54.529882: step 14500, loss = 0.835680 (77.2 examples/sec)\
=> 2018-12-17 05:40:35.943647: step 14600, loss = 1.098838 (77.3 examples/sec)\
=> 2018-12-17 05:41:17.301316: step 14700, loss = 0.840298 (77.4 examples/sec)\
=> 2018-12-17 05:41:58.649729: step 14800, loss = 0.324903 (77.4 examples/sec)\
=> 2018-12-17 05:42:39.986432: step 14900, loss = 0.367138 (77.4 examples/sec)\
=> 2018-12-17 05:43:21.380708: step 15000, loss = 0.911020 (77.3 examples/sec)\
==> accuracy = 0.891050, best accuracy 0.887398\
=> 2018-12-17 05:45:27.706448: step 15100, loss = 0.391932 (78.0 examples/sec)\
=> 2018-12-17 05:46:08.948237: step 15200, loss = 0.471621 (77.6 examples/sec)\
=> 2018-12-17 05:46:50.107138: step 15300, loss = 1.448636 (77.8 examples/sec)\
=> 2018-12-17 05:47:31.348001: step 15400, loss = 0.742364 (77.6 examples/sec)\
=> 2018-12-17 05:48:12.701374: step 15500, loss = 0.617247 (77.4 examples/sec)\
=> 2018-12-17 05:48:54.019827: step 15600, loss = 0.217673 (77.5 examples/sec)\
=> 2018-12-17 05:49:35.466274: step 15700, loss = 0.960790 (77.2 examples/sec)\
=> 2018-12-17 05:50:16.841519: step 15800, loss = 0.247452 (77.3 examples/sec)\
=> 2018-12-17 05:50:58.198419: step 15900, loss = 0.653705 (77.4 examples/sec)\
=> 2018-12-17 05:51:39.379829: step 16000, loss = 0.604676 (77.7 examples/sec)\
==> accuracy = 0.895593, best accuracy 0.891050\
=> 2018-12-17 05:53:47.634868: step 16100, loss = 0.631776 (77.9 examples/sec)\
=> 2018-12-17 05:54:28.738130: step 16200, loss = 0.244886 (77.9 examples/sec)\
=> 2018-12-17 05:55:09.963810: step 16300, loss = 0.356573 (77.6 examples/sec)\
=> 2018-12-17 05:55:51.158862: step 16400, loss = 0.623840 (77.7 examples/sec)\
=> 2018-12-17 05:56:32.379483: step 16500, loss = 0.531593 (77.6 examples/sec)\
=> 2018-12-17 05:57:13.646465: step 16600, loss = 0.129975 (77.6 examples/sec)\
=> 2018-12-17 05:57:54.919124: step 16700, loss = 0.259022 (77.5 examples/sec)\
=> 2018-12-17 05:58:36.189438: step 16800, loss = 0.635286 (77.5 examples/sec)\
=> 2018-12-17 05:59:17.444783: step 16900, loss = 0.628294 (77.6 examples/sec)\
=> 2018-12-17 05:59:58.831608: step 17000, loss = 0.522621 (77.3 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.899966, best accuracy 0.895593\
=> Model saved to file: ./logs/train/model.ckpt-17000\
"

model_text_4="\
Start training\
=> 2018-12-16 06:59:47.703112: step 100, loss = 7.701798 (82.4 examples/sec)\
=> 2018-12-16 07:00:12.070114: step 200, loss = 7.744798 (131.3 examples/sec)\
=> 2018-12-16 07:00:36.299441: step 300, loss = 6.696232 (132.1 examples/sec)\
=> 2018-12-16 07:01:00.422626: step 400, loss = 7.081499 (132.7 examples/sec)\
=> 2018-12-16 07:01:24.629075: step 500, loss = 6.594115 (132.2 examples/sec)\
=> 2018-12-16 07:01:48.949471: step 600, loss = 6.956951 (131.6 examples/sec)\
=> 2018-12-16 07:02:13.259391: step 700, loss = 7.079244 (131.7 examples/sec)\
=> 2018-12-16 07:02:37.651256: step 800, loss = 7.109058 (131.2 examples/sec)\
=> 2018-12-16 07:03:02.380957: step 900, loss = 6.080149 (129.4 examples/sec)\
=> 2018-12-16 07:03:26.937994: step 1000, loss = 6.854435 (130.3 examples/sec)\
=> Evaluating on validation dataset...\
WARNING:tensorflow:From /home/ecbm4040/SVHNClassifier/donkey.py:48: batch (from tensorflow.python.training.input) is deprecated and will be removed in a future version.\
Instructions for updating:\
Queue-based input pipelines have been replaced by `tf.data`. Use `tf.data.Dataset.batch(batch_size)` (or `padded_batch(...)` if `dynamic_pad=True`).\
(128, 18, 18, 48)\
(128, 9, 9, 64)\
(128, 9, 9, 128)\
(128, 9, 9, 160)\
(128, 5, 5, 192)\
(128, 5, 5, 192)\
(128, 3, 3, 192)\
==> accuracy = 0.013556, best accuracy 0.000000\
=> Model saved to file: ./logs/train/model.ckpt-1000\
=> patience = 100\
=> 2018-12-16 07:04:32.334873: step 1100, loss = 5.739432 (130.3 examples/sec)\
=> 2018-12-16 07:04:57.254891: step 1200, loss = 6.761232 (128.4 examples/sec)\
=> 2018-12-16 07:05:21.721214: step 1300, loss = 7.219971 (130.8 examples/sec)\
=> 2018-12-16 07:05:46.223091: step 1400, loss = 6.066162 (130.6 examples/sec)\
=> 2018-12-16 07:06:10.687554: step 1500, loss = 6.597883 (130.8 examples/sec)\
=> 2018-12-16 07:06:35.094334: step 1600, loss = 5.851267 (131.1 examples/sec)\
=> 2018-12-16 07:06:59.334326: step 1700, loss = 6.155232 (132.0 examples/sec)\
=> 2018-12-16 07:07:23.517997: step 1800, loss = 6.545037 (132.3 examples/sec)\
=> 2018-12-16 07:07:47.698534: step 1900, loss = 6.520647 (132.4 examples/sec)\
=> 2018-12-16 07:08:12.143363: step 2000, loss = 6.789651 (130.9 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.021453, best accuracy 0.013556\
=> Model saved to file: ./logs/train/model.ckpt-2000\
=> patience = 100\
=> 2018-12-16 07:09:17.181092: step 2100, loss = 6.366210 (132.1 examples/sec)\
=> 2018-12-16 07:09:41.514739: step 2200, loss = 5.627327 (131.5 examples/sec)\
=> 2018-12-16 07:10:06.099066: step 2300, loss = 5.899305 (130.2 examples/sec)\
=> 2018-12-16 07:10:30.477612: step 2400, loss = 5.910143 (131.3 examples/sec)\
=> 2018-12-16 07:10:54.789451: step 2500, loss = 6.528865 (131.6 examples/sec)\
=> 2018-12-16 07:11:19.164378: step 2600, loss = 4.890659 (131.3 examples/sec)\
=> 2018-12-16 07:11:43.592041: step 2700, loss = 6.297254 (131.0 examples/sec)\
=> 2018-12-16 07:12:08.024009: step 2800, loss = 6.803662 (131.0 examples/sec)\
=> 2018-12-16 07:12:32.522639: step 2900, loss = 5.665932 (130.6 examples/sec)\
=> 2018-12-16 07:12:56.969899: step 3000, loss = 6.388339 (130.9 examples/sec)\
=> Evaluating on validation dataset...\
(128, 18, 18, 48)\
(128, 9, 9, 64)\
(128, 9, 9, 128)\
(128, 9, 9, 160)\
(128, 5, 5, 192)\
(128, 5, 5, 192)\
(128, 3, 3, 192)\
==> accuracy = 0.051520, best accuracy 0.021453\
=> Model saved to file: ./logs/train/model.ckpt-3000\
=> patience = 100\
=> 2018-12-16 07:14:02.407763: step 3100, loss = 5.271324 (130.4 examples/sec)\
=> 2018-12-16 07:14:26.845030: step 3200, loss = 4.692977 (131.0 examples/sec)\
=> 2018-12-16 07:14:51.290732: step 3300, loss = 5.877679 (130.9 examples/sec)\
=> 2018-12-16 07:15:16.000552: step 3400, loss = 5.580437 (129.5 examples/sec)\
=> 2018-12-16 07:15:40.650100: step 3500, loss = 5.379105 (129.8 examples/sec)\
=> 2018-12-16 07:16:05.133452: step 3600, loss = 5.016535 (130.7 examples/sec)\
=> 2018-12-16 07:16:29.505509: step 3700, loss = 6.037333 (131.3 examples/sec)\
=> 2018-12-16 07:16:53.824757: step 3800, loss = 4.895581 (131.6 examples/sec)\
=> 2018-12-16 07:17:18.177615: step 3900, loss = 5.652240 (131.4 examples/sec)\
=> 2018-12-16 07:17:42.572642: step 4000, loss = 5.028730 (131.2 examples/sec)\
(128, 18, 18, 48)\
(128, 9, 9, 64)\
(128, 9, 9, 128)\
(128, 9, 9, 160)\
(128, 5, 5, 192)\
(128, 5, 5, 192)\
(128, 3, 3, 192)\
==> accuracy = 0.112627, best accuracy 0.051520\
=> Model saved to file: ./logs/train/model.ckpt-4000\
=> patience = 100\
=> 2018-12-16 07:18:47.775901: step 4100, loss = 5.006009 (131.7 examples/sec)\
=> 2018-12-16 07:19:12.059175: step 4200, loss = 5.350583 (131.8 examples/sec)\
=> 2018-12-16 07:19:36.317709: step 4300, loss = 4.614122 (131.9 examples/sec)\
=> 2018-12-16 07:20:00.698421: step 4400, loss = 4.107113 (131.3 examples/sec)\
=> 2018-12-16 07:20:25.255190: step 4500, loss = 4.038536 (130.3 examples/sec)\
=> 2018-12-16 07:20:49.683656: step 4600, loss = 4.444891 (131.0 examples/sec)\
=> 2018-12-16 07:21:13.962533: step 4700, loss = 3.585561 (131.8 examples/sec)\
=> 2018-12-16 07:21:38.182502: step 4800, loss = 4.216354 (132.1 examples/sec)\
=> 2018-12-16 07:22:02.479645: step 4900, loss = 5.184404 (131.7 examples/sec)\
=> 2018-12-16 07:22:26.691522: step 5000, loss = 3.478750 (132.2 examples/sec)\
=> Model saved to file: ./logs/train/model.ckpt-5000\
=> 2018-12-16 07:23:32.928957: step 5100, loss = 4.411841 (130.4 examples/sec)\
=> 2018-12-16 07:23:57.203279: step 5200, loss = 4.701019 (131.8 examples/sec)\
=> 2018-12-16 07:24:21.576055: step 5300, loss = 4.084748 (131.3 examples/sec)\
=> 2018-12-16 07:24:45.902365: step 5400, loss = 3.894312 (131.6 examples/sec)\
=> 2018-12-16 07:25:10.260895: step 5500, loss = 4.282209 (131.4 examples/sec)\
=> 2018-12-16 07:25:34.705085: step 5600, loss = 3.259143 (130.9 examples/sec)\
=> 2018-12-16 07:25:59.219871: step 5700, loss = 4.027782 (130.6 examples/sec)\
=> 2018-12-16 07:26:23.515133: step 5800, loss = 2.473343 (131.7 examples/sec)\
=> 2018-12-16 07:26:47.881747: step 5900, loss = 5.307797 (131.3 examples/sec)\
=> 2018-12-16 07:27:12.248433: step 6000, loss = 3.617081 (131.3 examples/sec)\
==> accuracy = 0.309333, best accuracy 0.203167\
=> Model saved to file: ./logs/train/model.ckpt-6000\
=> 2018-12-16 07:28:18.538541: step 6100, loss = 3.861762 (131.4 examples/sec)\
=> 2018-12-16 07:28:43.100091: step 6200, loss = 3.307383 (130.3 examples/sec)\
=> 2018-12-16 07:29:07.559092: step 6300, loss = 3.975829 (130.9 examples/sec)\
=> 2018-12-16 07:29:31.910614: step 6400, loss = 3.299411 (131.4 examples/sec)\
=> 2018-12-16 07:29:56.254330: step 6500, loss = 2.572351 (131.5 examples/sec)\
=> 2018-12-16 07:30:20.665343: step 6600, loss = 3.508308 (131.1 examples/sec)\
=> 2018-12-16 07:30:45.344650: step 6700, loss = 2.514903 (129.7 examples/sec)\
=> 2018-12-16 07:31:09.915563: step 6800, loss = 3.654827 (130.3 examples/sec)\
=> 2018-12-16 07:31:34.446203: step 6900, loss = 3.449766 (130.5 examples/sec)\
=> 2018-12-16 07:31:58.884962: step 7000, loss = 3.001015 (131.0 examples/sec)\
==> accuracy = 0.423522, best accuracy 0.309333\
=> Model saved to file: ./logs/train/model.ckpt-7000\
=> patience = 100\
=> 2018-12-16 07:33:05.328616: step 7100, loss = 2.784962 (130.9 examples/sec)\
=> 2018-12-16 07:33:29.948286: step 7200, loss = 3.855580 (130.0 examples/sec)\
=> 2018-12-16 07:33:54.500954: step 7300, loss = 2.745274 (130.4 examples/sec)\
=> 2018-12-16 07:34:18.944025: step 7400, loss = 3.299371 (130.9 examples/sec)\
=> 2018-12-16 07:34:43.509167: step 7500, loss = 2.583005 (130.3 examples/sec)\
=> 2018-12-16 07:35:07.989790: step 7600, loss = 2.221308 (130.7 examples/sec)\
=> 2018-12-16 07:35:32.498757: step 7700, loss = 2.630437 (130.6 examples/sec)\
=> 2018-12-16 07:35:57.249879: step 7800, loss = 2.985293 (129.3 examples/sec)\
=> 2018-12-16 07:36:21.771054: step 7900, loss = 2.185781 (130.5 examples/sec)\
=> 2018-12-16 07:36:46.273148: step 8000, loss = 1.994677 (130.6 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.509291, best accuracy 0.423522\
=> Model saved to file: ./logs/train/model.ckpt-8000\
=> patience = 100\
=> 2018-12-16 07:37:52.795797: step 8100, loss = 2.000218 (130.6 examples/sec)\
=> 2018-12-16 07:38:17.355719: step 8200, loss = 3.298908 (130.3 examples/sec)\
=> 2018-12-16 07:38:42.116305: step 8300, loss = 2.214887 (129.3 examples/sec)\
=> 2018-12-16 07:39:06.643337: step 8400, loss = 1.463960 (130.5 examples/sec)\
=> 2018-12-16 07:39:31.190883: step 8500, loss = 2.109309 (130.4 examples/sec)\
=> 2018-12-16 07:39:55.758406: step 8600, loss = 2.818695 (130.3 examples/sec)\
=> 2018-12-16 07:40:20.349947: step 8700, loss = 2.020982 (130.1 examples/sec)\
=> 2018-12-16 07:40:44.796393: step 8800, loss = 2.152629 (130.9 examples/sec)\
=> 2018-12-16 07:41:09.686290: step 8900, loss = 1.626450 (128.6 examples/sec)\
=> 2018-12-16 07:41:34.272331: step 9000, loss = 2.954205 (130.2 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.563387, best accuracy 0.509291\
=> Model saved to file: ./logs/train/model.ckpt-9000\
=> patience = 100\
=> 2018-12-16 07:42:39.722537: step 9100, loss = 2.170624 (130.8 examples/sec)\
=> 2018-12-16 07:43:04.336650: step 9200, loss = 1.511289 (130.0 examples/sec)\
=> 2018-12-16 07:43:28.941345: step 9300, loss = 2.354064 (130.1 examples/sec)\
=> 2018-12-16 07:43:53.781090: step 9400, loss = 2.678857 (128.8 examples/sec)\
=> 2018-12-16 07:44:18.376802: step 9500, loss = 2.127884 (130.1 examples/sec)\
=> 2018-12-16 07:44:42.993501: step 9600, loss = 1.968196 (130.0 examples/sec)\
=> 2018-12-16 07:45:07.551790: step 9700, loss = 1.713897 (130.3 examples/sec)\
=> 2018-12-16 07:45:32.117038: step 9800, loss = 1.265634 (130.3 examples/sec)\
=> 2018-12-16 07:45:56.674528: step 9900, loss = 2.577561 (130.3 examples/sec)\
=> 2018-12-16 07:46:21.622771: step 10000, loss = 1.732341 (128.3 examples/sec)\
==> accuracy = 0.608657, best accuracy 0.563387\
=> Model saved to file: ./logs/train/model.ckpt-10000\
=> patience = 100\
=> 2018-12-16 07:47:27.187456: step 10100, loss = 2.008230 (130.5 examples/sec)\
=> 2018-12-16 07:47:51.799788: step 10200, loss = 1.635729 (130.0 examples/sec)\
=> 2018-12-16 07:48:16.416063: step 10300, loss = 2.237031 (130.0 examples/sec)\
=> 2018-12-16 07:48:40.903831: step 10400, loss = 1.525203 (130.7 examples/sec)\
=> 2018-12-16 07:49:05.620725: step 10500, loss = 1.579553 (129.5 examples/sec)\
=> 2018-12-16 07:49:30.081654: step 10600, loss = 2.098098 (130.8 examples/sec)\
=> 2018-12-16 07:49:54.605186: step 10700, loss = 1.767111 (130.5 examples/sec)\
=> 2018-12-16 07:50:19.159889: step 10800, loss = 1.806753 (130.3 examples/sec)\
=> 2018-12-16 07:50:43.707303: step 10900, loss = 1.328848 (130.4 examples/sec)\
=> 2018-12-16 07:51:08.328636: step 11000, loss = 1.162111 (130.0 examples/sec)\
==> accuracy = 0.663387, best accuracy 0.608657\
=> Model saved to file: ./logs/train/model.ckpt-11000\
=> 2018-12-16 07:52:14.128575: step 11100, loss = 1.315747 (129.7 examples/sec)\
=> 2018-12-16 07:52:38.797692: step 11200, loss = 1.304263 (129.7 examples/sec)\
=> 2018-12-16 07:53:03.378319: step 11300, loss = 2.459518 (130.2 examples/sec)\
=> 2018-12-16 07:53:28.048574: step 11400, loss = 1.180325 (129.7 examples/sec)\
=> 2018-12-16 07:53:52.825099: step 11500, loss = 1.330799 (129.2 examples/sec)\
=> 2018-12-16 07:54:17.592189: step 11600, loss = 1.985771 (129.2 examples/sec)\
=> 2018-12-16 07:54:42.143248: step 11700, loss = 1.012622 (130.4 examples/sec)\
=> 2018-12-16 07:55:06.717718: step 11800, loss = 1.193989 (130.2 examples/sec)\
=> 2018-12-16 07:55:31.282143: step 11900, loss = 2.574837 (130.3 examples/sec)\
=> 2018-12-16 07:55:55.876722: step 12000, loss = 1.457171 (130.1 examples/sec)\
==> accuracy = 0.679730, best accuracy 0.663387\
=> Model saved to file: ./logs/train/model.ckpt-12000\
=> patience = 100\
=> 2018-12-16 07:57:01.599143: step 12100, loss = 1.091861 (129.4 examples/sec)\
=> 2018-12-16 07:57:26.154566: step 12200, loss = 1.566029 (130.3 examples/sec)\
=> 2018-12-16 07:57:50.708837: step 12300, loss = 1.213231 (130.3 examples/sec)\
=> 2018-12-16 07:58:15.271034: step 12400, loss = 1.246663 (130.3 examples/sec)\
=> 2018-12-16 07:58:39.937676: step 12500, loss = 1.527319 (129.8 examples/sec)\
=> 2018-12-16 07:59:04.727036: step 12600, loss = 1.726992 (129.1 examples/sec)\
=> 2018-12-16 07:59:29.312367: step 12700, loss = 3.127095 (130.2 examples/sec)\
=> 2018-12-16 07:59:53.876896: step 12800, loss = 1.941799 (130.3 examples/sec)\
=> 2018-12-16 08:00:18.399094: step 12900, loss = 1.636216 (130.5 examples/sec)\
=> 2018-12-16 08:00:42.974235: step 13000, loss = 2.159415 (130.2 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.680448, best accuracy 0.679730\
=> Model saved to file: ./logs/train/model.ckpt-13000\
=> patience = 100\
=> 2018-12-16 08:01:48.630257: step 13100, loss = 1.505587 (128.9 examples/sec)\
=> 2018-12-16 08:02:13.237293: step 13200, loss = 1.931212 (130.1 examples/sec)\
=> 2018-12-16 08:02:37.837814: step 13300, loss = 1.764505 (130.1 examples/sec)\
=> 2018-12-16 08:03:02.381497: step 13400, loss = 1.278157 (130.4 examples/sec)\
=> 2018-12-16 08:03:26.937522: step 13500, loss = 1.290407 (130.3 examples/sec)\
=> 2018-12-16 08:03:51.576802: step 13600, loss = 1.233401 (129.9 examples/sec)\
=> 2018-12-16 08:04:16.342531: step 13700, loss = 1.160871 (129.2 examples/sec)\
=> 2018-12-16 08:04:40.921293: step 13800, loss = 1.826124 (130.2 examples/sec)\
=> 2018-12-16 08:05:05.549244: step 13900, loss = 0.823147 (130.0 examples/sec)\
=> 2018-12-16 08:05:30.141739: step 14000, loss = 1.844455 (130.1 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.713049, best accuracy 0.680448\
=> Model saved to file: ./logs/train/model.ckpt-14000\
=> patience = 100\
=> 2018-12-16 08:06:35.729806: step 14100, loss = 2.936877 (129.9 examples/sec)\
=> 2018-12-16 08:07:00.698590: step 14200, loss = 1.658607 (128.2 examples/sec)\
=> 2018-12-16 08:07:25.276711: step 14300, loss = 1.116484 (130.2 examples/sec)\
=> 2018-12-16 08:07:49.839923: step 14400, loss = 1.566609 (130.3 examples/sec)\
=> 2018-12-16 08:08:14.408302: step 14500, loss = 2.522209 (130.3 examples/sec)\
=> 2018-12-16 08:08:38.859122: step 14600, loss = 1.199162 (130.9 examples/sec)\
=> 2018-12-16 08:09:03.319208: step 14700, loss = 2.326551 (130.8 examples/sec)\
=> 2018-12-16 08:09:28.053571: step 14800, loss = 0.694364 (129.4 examples/sec)\
=> 2018-12-16 08:09:52.563575: step 14900, loss = 1.147221 (130.6 examples/sec)\
=> 2018-12-16 08:10:17.064808: step 15000, loss = 0.982057 (130.6 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.720861, best accuracy 0.713049\
=> Model saved to file: ./logs/train/model.ckpt-15000\
=> patience = 100\
=> 2018-12-16 08:11:23.343868: step 15100, loss = 1.449319 (130.8 examples/sec)\
=> 2018-12-16 08:11:47.841802: step 15200, loss = 1.909352 (130.6 examples/sec)\
=> 2018-12-16 08:12:12.750491: step 15300, loss = 0.554543 (128.5 examples/sec)\
=> 2018-12-16 08:12:37.292253: step 15400, loss = 1.069300 (130.4 examples/sec)\
=> 2018-12-16 08:13:01.773132: step 15500, loss = 1.516402 (130.7 examples/sec)\
=> 2018-12-16 08:13:26.312738: step 15600, loss = 1.228088 (130.4 examples/sec)\
=> 2018-12-16 08:13:50.809378: step 15700, loss = 1.163167 (130.7 examples/sec)\
=> 2018-12-16 08:14:15.492166: step 15800, loss = 2.079050 (129.7 examples/sec)\
=> 2018-12-16 08:14:40.019499: step 15900, loss = 1.092090 (130.5 examples/sec)\
=> 2018-12-16 08:15:04.518270: step 16000, loss = 0.982890 (130.6 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.743877, best accuracy 0.720861\
=> Model saved to file: ./logs/train/model.ckpt-16000\
=> patience = 100\
=> 2018-12-16 08:16:10.935243: step 16100, loss = 1.318922 (130.4 examples/sec)\
=> 2018-12-16 08:16:35.462082: step 16200, loss = 0.967894 (130.5 examples/sec)\
=> 2018-12-16 08:17:00.015736: step 16300, loss = 0.949065 (130.3 examples/sec)\
=> 2018-12-16 08:17:24.863335: step 16400, loss = 1.356506 (128.8 examples/sec)\
=> 2018-12-16 08:17:49.432692: step 16500, loss = 1.606587 (130.3 examples/sec)\
=> 2018-12-16 08:18:14.004685: step 16600, loss = 1.414560 (130.3 examples/sec)\
=> 2018-12-16 08:18:38.653481: step 16700, loss = 1.037161 (129.8 examples/sec)\
=> 2018-12-16 08:19:03.185842: step 16800, loss = 1.462920 (130.5 examples/sec)\
=> 2018-12-16 08:19:27.963388: step 16900, loss = 0.620479 (129.2 examples/sec)\
=> 2018-12-16 08:19:52.502083: step 17000, loss = 0.654510 (130.4 examples/sec)\
==> accuracy = 0.755532, best accuracy 0.743877\
=> Model saved to file: ./logs/train/model.ckpt-17000\
=> patience = 100\
=> 2018-12-16 08:20:57.680288: step 17100, loss = 1.338733 (130.9 examples/sec)\
=> 2018-12-16 08:21:22.104278: step 17200, loss = 1.482820 (131.0 examples/sec)\
=> 2018-12-16 08:21:46.628327: step 17300, loss = 1.031446 (130.5 examples/sec)\
=> 2018-12-16 08:22:11.036444: step 17400, loss = 1.134689 (131.1 examples/sec)\
=> 2018-12-16 08:22:35.814151: step 17500, loss = 0.692101 (129.2 examples/sec)\
=> 2018-12-16 08:23:00.311615: step 17600, loss = 2.222630 (130.6 examples/sec)\
=> 2018-12-16 08:23:24.895260: step 17700, loss = 1.434030 (130.2 examples/sec)\
=> 2018-12-16 08:23:49.342321: step 17800, loss = 0.953320 (130.9 examples/sec)\
=> 2018-12-16 08:24:13.833965: step 17900, loss = 0.713514 (130.7 examples/sec)\
=> 2018-12-16 08:24:38.569092: step 18000, loss = 1.160778 (129.4 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.761867, best accuracy 0.755532\
=> Model saved to file: ./logs/train/model.ckpt-18000\
=> patience = 100\
=> 2018-12-16 08:25:45.085027: step 18100, loss = 1.075515 (130.6 examples/sec)\
=> 2018-12-16 08:26:09.465932: step 18200, loss = 0.542642 (131.3 examples/sec)\
=> 2018-12-16 08:26:33.889361: step 18300, loss = 1.209105 (131.0 examples/sec)\
=> 2018-12-16 08:26:58.486374: step 18400, loss = 1.514152 (130.1 examples/sec)\
=> 2018-12-16 08:27:22.909122: step 18500, loss = 1.140725 (131.0 examples/sec)\
=> 2018-12-16 08:27:47.727266: step 18600, loss = 0.579860 (129.0 examples/sec)\
=> 2018-12-16 08:28:12.209232: step 18700, loss = 1.242218 (130.7 examples/sec)\
=> 2018-12-16 08:28:36.688144: step 18800, loss = 1.040309 (130.7 examples/sec)\
=> 2018-12-16 08:29:01.097326: step 18900, loss = 0.904664 (131.1 examples/sec)\
=> 2018-12-16 08:29:25.667036: step 19000, loss = 0.944068 (130.3 examples/sec)\
==> accuracy = 0.772677, best accuracy 0.761867\
=> Model saved to file: ./logs/train/model.ckpt-19000\
=> patience = 100\
=> 2018-12-16 08:30:32.166092: step 19100, loss = 1.577386 (130.8 examples/sec)\
=> 2018-12-16 08:30:56.521639: step 19200, loss = 1.152827 (131.4 examples/sec)\
=> 2018-12-16 08:31:21.051433: step 19300, loss = 2.037206 (130.5 examples/sec)\
=> 2018-12-16 08:31:45.529454: step 19400, loss = 0.559047 (130.8 examples/sec)\
=> 2018-12-16 08:32:09.963630: step 19500, loss = 0.794345 (131.0 examples/sec)\
=> 2018-12-16 08:32:34.439195: step 19600, loss = 1.126701 (130.8 examples/sec)\
=> 2018-12-16 08:32:59.249616: step 19700, loss = 1.164702 (129.0 examples/sec)\
=> 2018-12-16 08:33:23.746996: step 19800, loss = 1.148179 (130.6 examples/sec)\
=> 2018-12-16 08:33:48.245108: step 19900, loss = 0.549017 (130.6 examples/sec)\
=> 2018-12-16 08:34:12.673074: step 20000, loss = 1.222575 (131.0 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.780152, best accuracy 0.772677\
=> Model saved to file: ./logs/train/model.ckpt-20000\
=> patience = 100\
=> 2018-12-16 08:35:18.168617: step 20100, loss = 0.792453 (131.0 examples/sec)\
=> 2018-12-16 08:35:42.611970: step 20200, loss = 1.009639 (130.9 examples/sec)\
=> 2018-12-16 08:36:07.012335: step 20300, loss = 0.657414 (131.2 examples/sec)\
=> 2018-12-16 08:36:31.442012: step 20400, loss = 1.939332 (131.0 examples/sec)\
=> 2018-12-16 08:36:55.888598: step 20500, loss = 0.687870 (130.9 examples/sec)\
=> 2018-12-16 08:37:20.404422: step 20600, loss = 1.601103 (130.5 examples/sec)\
=> 2018-12-16 08:37:44.910121: step 20700, loss = 0.911445 (130.6 examples/sec)\
=> 2018-12-16 08:38:09.757697: step 20800, loss = 0.533030 (128.8 examples/sec)\
=> 2018-12-16 08:38:34.157905: step 20900, loss = 0.535794 (131.2 examples/sec)\
=> 2018-12-16 08:38:58.540535: step 21000, loss = 0.680010 (131.3 examples/sec)\
==> accuracy = 0.794552, best accuracy 0.780152\
=> Model saved to file: ./logs/train/model.ckpt-21000\
=> patience = 100\
=> 2018-12-16 08:40:04.040591: step 21100, loss = 0.614217 (130.0 examples/sec)\
=> 2018-12-16 08:40:28.587917: step 21200, loss = 0.270524 (130.4 examples/sec)\
=> 2018-12-16 08:40:53.068787: step 21300, loss = 0.425993 (130.7 examples/sec)\
=> 2018-12-16 08:41:17.521722: step 21400, loss = 1.712447 (130.9 examples/sec)\
=> 2018-12-16 08:41:41.966208: step 21500, loss = 1.003389 (130.9 examples/sec)\
=> 2018-12-16 08:42:06.410077: step 21600, loss = 1.565685 (130.9 examples/sec)\
=> 2018-12-16 08:42:30.845350: step 21700, loss = 0.488050 (131.0 examples/sec)\
=> 2018-12-16 08:42:55.259662: step 21800, loss = 2.386770 (131.1 examples/sec)\
=> 2018-12-16 08:43:20.111972: step 21900, loss = 0.491588 (128.8 examples/sec)\
=> 2018-12-16 08:43:44.538651: step 22000, loss = 0.759491 (131.0 examples/sec)\
==> accuracy = 0.815372, best accuracy 0.794552\
=> Model saved to file: ./logs/train/model.ckpt-22000\
=> patience = 100\
=> 2018-12-16 08:44:50.171192: step 22100, loss = 1.102410 (129.6 examples/sec)\
=> 2018-12-16 08:45:14.700481: step 22200, loss = 0.924387 (130.5 examples/sec)\
=> 2018-12-16 08:45:39.272968: step 22300, loss = 0.496836 (130.2 examples/sec)\
=> 2018-12-16 08:46:03.883200: step 22400, loss = 1.444788 (130.0 examples/sec)\
=> 2018-12-16 08:46:28.438408: step 22500, loss = 2.100366 (130.3 examples/sec)\
=> 2018-12-16 08:46:53.066264: step 22600, loss = 1.113616 (130.0 examples/sec)\
=> 2018-12-16 08:47:17.664268: step 22700, loss = 1.063558 (130.1 examples/sec)\
=> 2018-12-16 08:47:42.228953: step 22800, loss = 1.427073 (130.3 examples/sec)\
=> 2018-12-16 08:48:06.840808: step 22900, loss = 0.997064 (130.0 examples/sec)\
=> 2018-12-16 08:48:31.738886: step 23000, loss = 0.391360 (128.5 examples/sec)\
=> Evaluating on validation dataset...\
==> accuracy = 0.812458, best accuracy 0.815372\
=> patience = 99\
=> 2018-12-16 08:49:36.811547: step 23100, loss = 0.691780 (130.7 examples/sec)\
=> 2018-12-16 08:50:01.556517: step 23200, loss = 1.400455 (129.3 examples/sec)\
=> 2018-12-16 08:50:25.999646: step 23300, loss = 0.532196 (130.9 examples/sec)\
=> 2018-12-16 08:50:50.503972: step 23400, loss = 0.965914 (130.6 examples/sec)\
=> 2018-12-16 08:51:15.039758: step 23500, loss = 1.017144 (130.4 examples/sec)\
=> 2018-12-16 08:51:39.635659: step 23600, loss = 0.679947 (130.1 examples/sec)\
=> 2018-12-16 08:52:04.103340: step 23700, loss = 1.238580 (130.8 examples/sec)\
=> 2018-12-16 08:52:28.552502: step 23800, loss = 1.025028 (130.9 examples/sec)\
=> 2018-12-16 08:52:52.998867: step 23900, loss = 1.146688 (130.9 examples/sec)\
=> 2018-12-16 08:53:17.552019: step 24000, loss = 0.986271 (130.4 examples/sec)\
==> accuracy = 0.814358, best accuracy 0.815372\
=> patience = 98\
=> 2018-12-16 08:54:22.821788: step 24100, loss = 1.709477 (130.4 examples/sec)\
=> 2018-12-16 08:54:47.329095: step 24200, loss = 0.835984 (130.6 examples/sec)\
=> 2018-12-16 08:55:12.073991: step 24300, loss = 1.064946 (129.3 examples/sec)\
=> 2018-12-16 08:55:36.634287: step 24400, loss = 1.540593 (130.3 examples/sec)\
=> 2018-12-16 08:56:01.176031: step 24500, loss = 0.238730 (130.4 examples/sec)\
=> 2018-12-16 08:56:25.716545: step 24600, loss = 0.571602 (130.4 examples/sec)\
=> 2018-12-16 08:56:50.207614: step 24700, loss = 1.041020 (130.7 examples/sec)\
=> 2018-12-16 08:57:14.693889: step 24800, loss = 1.428196 (130.7 examples/sec)\
=> 2018-12-16 08:57:39.214689: step 24900, loss = 0.401121 (130.5 examples/sec)\
=> 2018-12-16 08:58:03.689309: step 25000, loss = 1.201278 (130.8 examples/sec)\
==> accuracy = 0.802618, best accuracy 0.815372\
=> patience = 97\
=> 2018-12-16 08:59:08.923614: step 25100, loss = 0.648055 (130.5 examples/sec)\
=> 2018-12-16 08:59:33.380656: step 25200, loss = 2.060895 (130.9 examples/sec)\
=> 2018-12-16 08:59:57.901960: step 25300, loss = 0.225090 (130.5 examples/sec)\
=> 2018-12-16 09:00:22.693695: step 25400, loss = 0.605206 (129.1 examples/sec)\
=> 2018-12-16 09:00:47.168301: step 25500, loss = 0.562875 (130.8 examples/sec)\
=> 2018-12-16 09:01:11.652126: step 25600, loss = 0.778907 (130.7 examples/sec)\
=> 2018-12-16 09:01:36.083562: step 25700, loss = 1.074082 (131.0 examples/sec)\
=> 2018-12-16 09:02:00.498458: step 25800, loss = 0.988692 (131.1 examples/sec)\
=> 2018-12-16 09:02:24.965660: step 25900, loss = 1.074567 (130.8 examples/sec)\
=> 2018-12-16 09:02:49.424222: step 26000, loss = 1.401141 (130.9 examples/sec)\
==> accuracy = 0.824367, best accuracy 0.815372\
=> Model saved to file: ./logs/train/model.ckpt-26000\
=> patience = 100\
=> 2018-12-16 09:03:55.049287: step 26100, loss = 1.509478 (129.0 examples/sec)\
=> 2018-12-16 09:04:19.597417: step 26200, loss = 0.633090 (130.4 examples/sec)\
=> 2018-12-16 09:04:44.069989: step 26300, loss = 0.694507 (130.8 examples/sec)\
=> 2018-12-16 09:05:08.629777: step 26400, loss = 1.082859 (130.3 examples/sec)\
=> 2018-12-16 09:05:33.217137: step 26500, loss = 0.650416 (130.2 examples/sec)\
=> 2018-12-16 09:05:57.667451: step 26600, loss = 0.776979 (130.9 examples/sec)\
=> 2018-12-16 09:06:22.176434: step 26700, loss = 0.444958 (130.6 examples/sec)\
=> 2018-12-16 09:06:46.594110: step 26800, loss = 0.555668 (131.1 examples/sec)\
=> 2018-12-16 09:07:11.016403: step 26900, loss = 0.716004 (131.1 examples/sec)\
=> 2018-12-16 09:07:35.478124: step 27000, loss = 0.859185 (130.8 examples/sec)\
==> accuracy = 0.835220, best accuracy 0.824367\
=> Model saved to file: ./logs/train/model.ckpt-27000\
=> patience = 100\
=> 2018-12-16 09:08:40.632865: step 27100, loss = 0.774413 (131.5 examples/sec)\
=> 2018-12-16 09:09:05.520770: step 27200, loss = 0.428742 (128.6 examples/sec)\
=> 2018-12-16 09:09:29.953316: step 27300, loss = 0.913297 (131.0 examples/sec)\
=> 2018-12-16 09:09:54.422894: step 27400, loss = 0.563971 (130.8 examples/sec)\
=> 2018-12-16 09:10:19.111860: step 27500, loss = 0.977166 (129.6 examples/sec)\
=> 2018-12-16 09:10:43.553650: step 27600, loss = 1.330850 (130.9 examples/sec)\
=> 2018-12-16 09:11:07.915002: step 27700, loss = 0.262105 (131.4 examples/sec)\
=> 2018-12-16 09:11:32.339247: step 27800, loss = 0.462883 (131.0 examples/sec)\
=> 2018-12-16 09:11:56.778901: step 27900, loss = 1.225317 (131.0 examples/sec)\
=> 2018-12-16 09:12:21.151374: step 28000, loss = 1.486055 (131.3 examples/sec)\
==> accuracy = 0.833108, best accuracy 0.835220\
=> patience = 99\
=> 2018-12-16 09:13:25.938600: step 28100, loss = 0.182115 (131.1 examples/sec)\
=> 2018-12-16 09:13:50.418746: step 28200, loss = 0.734415 (130.7 examples/sec)\
=> 2018-12-16 09:14:15.260844: step 28300, loss = 0.716986 (128.8 examples/sec)\
=> 2018-12-16 09:14:39.734896: step 28400, loss = 0.814611 (130.8 examples/sec)\
=> 2018-12-16 09:15:04.178570: step 28500, loss = 1.835103 (130.9 examples/sec)\
=> 2018-12-16 09:15:28.877096: step 28600, loss = 1.114392 (129.6 examples/sec)\
=> 2018-12-16 09:15:53.310987: step 28700, loss = 0.713831 (131.0 examples/sec)\
=> 2018-12-16 09:16:17.854355: step 28800, loss = 0.404545 (130.4 examples/sec)\
=> 2018-12-16 09:16:42.251961: step 28900, loss = 1.196245 (131.2 examples/sec)\
=> 2018-12-16 09:17:06.741151: step 29000, loss = 0.534788 (130.7 examples/sec)\
==> accuracy = 0.838936, best accuracy 0.835220\
=> Model saved to file: ./logs/train/model.ckpt-29000\
=> patience = 100\
=> 2018-12-16 09:18:12.193417: step 29100, loss = 0.231495 (130.8 examples/sec)\
=> 2018-12-16 09:18:36.655067: step 29200, loss = 0.536239 (130.8 examples/sec)\
=> 2018-12-16 09:19:01.110196: step 29300, loss = 0.791559 (130.9 examples/sec)\
=> 2018-12-16 09:19:25.909868: step 29400, loss = 0.728662 (129.1 examples/sec)\
=> 2018-12-16 09:19:50.462993: step 29500, loss = 1.032256 (130.4 examples/sec)\
=> 2018-12-16 09:20:14.925948: step 29600, loss = 0.401376 (130.8 examples/sec)\
=> 2018-12-16 09:20:39.643644: step 29700, loss = 0.568919 (129.5 examples/sec)\
=> 2018-12-16 09:21:04.069785: step 29800, loss = 1.035080 (131.0 examples/sec)\
=> 2018-12-16 09:21:28.502142: step 29900, loss = 0.564480 (131.0 examples/sec)\
=> 2018-12-16 09:21:52.991352: step 30000, loss = 1.300985 (130.7 examples/sec)\
==> accuracy = 0.842230, best accuracy 0.838936\
=> Model saved to file: ./logs/train/model.ckpt-30000\
=> patience = 100\
=> 2018-12-16 09:22:59.169528: step 30100, loss = 0.932724 (131.5 examples/sec)\
=> 2018-12-16 09:23:23.567896: step 30200, loss = 1.025441 (131.2 examples/sec)\
=> 2018-12-16 09:23:48.030957: step 30300, loss = 0.745866 (130.8 examples/sec)\
=> 2018-12-16 09:24:12.471137: step 30400, loss = 0.286412 (131.0 examples/sec)\
=> 2018-12-16 09:24:37.220227: step 30500, loss = 0.837268 (129.3 examples/sec)\
=> 2018-12-16 09:25:01.664015: step 30600, loss = 0.335996 (130.9 examples/sec)\
=> 2018-12-16 09:25:26.102835: step 30700, loss = 0.476662 (131.0 examples/sec)\
=> 2018-12-16 09:25:50.626905: step 30800, loss = 0.441207 (130.5 examples/sec)\
=> 2018-12-16 09:26:14.956513: step 30900, loss = 0.561932 (131.5 examples/sec)\
=> 2018-12-16 09:26:39.411066: step 31000, loss = 0.471954 (130.9 examples/sec)\
(128, 3, 3, 192)\
==> accuracy = 0.831715, best accuracy 0.842230\
=> patience = 99\
=> 2018-12-16 09:27:44.397438: step 31100, loss = 1.162233 (130.9 examples/sec)\
=> 2018-12-16 09:28:08.824069: step 31200, loss = 0.175457 (131.0 examples/sec)\
=> 2018-12-16 09:28:33.249558: step 31300, loss = 0.651607 (131.0 examples/sec)\
=> 2018-12-16 09:28:57.684934: step 31400, loss = 0.936725 (131.0 examples/sec)\
=> 2018-12-16 09:29:22.136178: step 31500, loss = 1.493922 (130.9 examples/sec)\
=> 2018-12-16 09:29:46.899137: step 31600, loss = 0.676499 (129.2 examples/sec)\
=> 2018-12-16 09:30:11.388577: step 31700, loss = 0.908290 (130.7 examples/sec)\
=> 2018-12-16 09:30:35.890915: step 31800, loss = 1.274515 (130.6 examples/sec)\
=> 2018-12-16 09:31:00.383776: step 31900, loss = 1.029521 (130.7 examples/sec)\
=> 2018-12-16 09:31:24.821968: step 32000, loss = 1.009165 (131.0 examples/sec)\
==> accuracy = 0.854223, best accuracy 0.842230\
=> Model saved to file: ./logs/train/model.ckpt-32000\
=> patience = 100\
=> 2018-12-16 09:32:31.147608: step 32100, loss = 1.826051 (131.1 examples/sec)\
=> 2018-12-16 09:32:55.570595: step 32200, loss = 0.455118 (131.0 examples/sec)\
=> 2018-12-16 09:33:19.967753: step 32300, loss = 1.726859 (131.2 examples/sec)\
=> 2018-12-16 09:33:44.427313: step 32400, loss = 0.568630 (130.8 examples/sec)\
=> 2018-12-16 09:34:08.835787: step 32500, loss = 1.164672 (131.1 examples/sec)\
=> 2018-12-16 09:34:33.246080: step 32600, loss = 0.740348 (131.1 examples/sec)\
=> 2018-12-16 09:34:57.942349: step 32700, loss = 0.736144 (129.6 examples/sec)\
=> 2018-12-16 09:35:22.309614: step 32800, loss = 1.070662 (131.3 examples/sec)\
=> 2018-12-16 09:35:46.925950: step 32900, loss = 0.922417 (130.0 examples/sec)\
=> 2018-12-16 09:36:11.375677: step 33000, loss = 0.621156 (130.9 examples/sec)\
==> accuracy = 0.850338, best accuracy 0.854223\
=> patience = 99\
=> 2018-12-16 09:37:16.230671: step 33100, loss = 0.524972 (131.1 examples/sec)\
=> 2018-12-16 09:37:40.681846: step 33200, loss = 1.442573 (130.9 examples/sec)\
=> 2018-12-16 09:38:05.180796: step 33300, loss = 0.319752 (130.6 examples/sec)\
=> 2018-12-16 09:38:29.627352: step 33400, loss = 0.522246 (130.9 examples/sec)\
=> 2018-12-16 09:38:54.070707: step 33500, loss = 0.602032 (130.9 examples/sec)\
=> 2018-12-16 09:39:18.448974: step 33600, loss = 0.127526 (131.3 examples/sec)\
=> 2018-12-16 09:39:42.892693: step 33700, loss = 1.127924 (130.9 examples/sec)\
=> 2018-12-16 09:40:07.710665: step 33800, loss = 0.396698 (129.0 examples/sec)\
=> 2018-12-16 09:40:32.136642: step 33900, loss = 0.291941 (131.0 examples/sec)\
=> 2018-12-16 09:40:56.845642: step 34000, loss = 0.804136 (129.5 examples/sec)\
==> accuracy = 0.860051, best accuracy 0.854223\
=> Model saved to file: ./logs/train/model.ckpt-34000\
=> patience = 100\
=> 2018-12-16 09:42:02.102269: step 34100, loss = 0.589351 (130.9 examples/sec)\
=> 2018-12-16 09:42:26.529323: step 34200, loss = 0.622169 (131.0 examples/sec)\
=> 2018-12-16 09:42:50.851836: step 34300, loss = 0.671348 (131.6 examples/sec)\
=> 2018-12-16 09:43:15.268748: step 34400, loss = 0.883396 (131.1 examples/sec)\
=> 2018-12-16 09:43:39.632323: step 34500, loss = 0.622792 (131.4 examples/sec)\
=> 2018-12-16 09:44:04.008899: step 34600, loss = 0.543157 (131.3 examples/sec)\
=> 2018-12-16 09:44:28.374673: step 34700, loss = 0.493676 (131.4 examples/sec)\
=> 2018-12-16 09:44:52.820823: step 34800, loss = 2.261553 (130.9 examples/sec)\
=> 2018-12-16 09:45:17.522214: step 34900, loss = 0.873732 (129.6 examples/sec)\
=> 2018-12-16 09:45:42.020316: step 35000, loss = 0.937154 (130.6 examples/sec)\
==> accuracy = 0.845524, best accuracy 0.860051\
=> patience = 99\
=> 2018-12-16 09:46:47.172382: step 35100, loss = 0.729547 (130.6 examples/sec)\
=> 2018-12-16 09:47:11.521238: step 35200, loss = 1.085285 (131.4 examples/sec)\
=> 2018-12-16 09:47:36.008467: step 35300, loss = 0.558099 (130.7 examples/sec)\
=> 2018-12-16 09:48:00.482178: step 35400, loss = 0.470927 (130.8 examples/sec)\
=> 2018-12-16 09:48:24.918696: step 35500, loss = 0.574977 (131.0 examples/sec)\
=> 2018-12-16 09:48:49.395634: step 35600, loss = 0.287046 (130.8 examples/sec)\
=> 2018-12-16 09:49:13.847327: step 35700, loss = 0.497756 (130.9 examples/sec)\
=> 2018-12-16 09:49:38.350038: step 35800, loss = 0.407360 (130.6 examples/sec)\
=> 2018-12-16 09:50:02.797083: step 35900, loss = 0.642997 (130.9 examples/sec)\
=> 2018-12-16 09:50:27.527124: step 36000, loss = 0.527941 (129.4 examples/sec)\
==> accuracy = 0.861064, best accuracy 0.860051\
=> Model saved to file: ./logs/train/model.ckpt-36000\
=> patience = 100\
=> 2018-12-16 09:51:33.949622: step 36100, loss = 0.585236 (130.8 examples/sec)\
=> 2018-12-16 09:51:58.400333: step 36200, loss = 0.646806 (130.9 examples/sec)\
=> 2018-12-16 09:52:22.893404: step 36300, loss = 0.811019 (130.7 examples/sec)\
=> 2018-12-16 09:52:47.282121: step 36400, loss = 0.390549 (131.2 examples/sec)\
=> 2018-12-16 09:53:11.692018: step 36500, loss = 0.603356 (131.1 examples/sec)\
=> 2018-12-16 09:53:36.231444: step 36600, loss = 1.137289 (130.4 examples/sec)\
=> 2018-12-16 09:54:00.710249: step 36700, loss = 0.108867 (130.7 examples/sec)\
=> 2018-12-16 09:54:25.248598: step 36800, loss = 0.351628 (130.4 examples/sec)\
=> 2018-12-16 09:54:49.688201: step 36900, loss = 1.162235 (131.0 examples/sec)\
=> 2018-12-16 09:55:14.149767: step 37000, loss = 0.552735 (130.8 examples/sec)\
==> accuracy = 0.863851, best accuracy 0.861064\
=> Model saved to file: ./logs/train/model.ckpt-37000\
=> patience = 100\
=> 2018-12-16 09:56:19.909719: step 37100, loss = 1.298377 (129.8 examples/sec)\
=> 2018-12-16 09:56:44.361735: step 37200, loss = 0.684355 (130.9 examples/sec)\
=> 2018-12-16 09:57:08.787426: step 37300, loss = 0.599085 (131.0 examples/sec)\
=> 2018-12-16 09:57:33.192836: step 37400, loss = 0.348212 (131.1 examples/sec)\
=> 2018-12-16 09:57:57.605707: step 37500, loss = 0.567727 (131.1 examples/sec)\
=> 2018-12-16 09:58:22.042152: step 37600, loss = 1.451012 (131.0 examples/sec)\
=> 2018-12-16 09:58:46.517139: step 37700, loss = 0.902829 (130.8 examples/sec)\
=> 2018-12-16 09:59:10.957327: step 37800, loss = 0.571427 (131.0 examples/sec)\
=> 2018-12-16 09:59:35.489854: step 37900, loss = 0.845268 (130.5 examples/sec)\
=> 2018-12-16 09:59:59.833593: step 38000, loss = 0.664285 (131.5 examples/sec)\
==> accuracy = 0.860853, best accuracy 0.863851\
"

model33text="\
=> 2018-12-16 06:19:08.364939: step 100, loss = 7.802336 (51.2 examples/sec)\
=> 2018-12-16 06:19:53.103361: step 200, loss = 7.585062 (71.5 examples/sec)\
=> 2018-12-16 06:20:38.351416: step 300, loss = 6.083612 (70.7 examples/sec)\
=> 2018-12-16 06:21:24.128720: step 400, loss = 6.907388 (69.9 examples/sec)\
=> 2018-12-16 06:22:10.439699: step 500, loss = 7.131026 (69.1 examples/sec)\
=> 2018-12-16 06:22:55.628877: step 600, loss = 6.848192 (70.8 examples/sec)\
=> 2018-12-16 06:23:42.775478: step 700, loss = 6.403450 (67.9 examples/sec)\
=> 2018-12-16 06:24:27.778027: step 800, loss = 5.643059 (71.1 examples/sec)\
=> 2018-12-16 06:25:15.517511: step 900, loss = 5.073796 (67.0 examples/sec)\
=> 2018-12-16 06:26:01.642228: step 1000, loss = 5.121696 (69.4 examples/sec)\
==> accuracy = 0.079823, best accuracy 0.000000\
=> 2018-12-16 06:28:22.530679: step 1100, loss = 5.320220 (67.8 examples/sec)\
=> 2018-12-16 06:29:09.432766: step 1200, loss = 4.367892 (68.2 examples/sec)\
=> 2018-12-16 06:29:56.233060: step 1300, loss = 4.568501 (68.4 examples/sec)\
=> 2018-12-16 06:30:42.472538: step 1400, loss = 4.140320 (69.2 examples/sec)\
=> 2018-12-16 06:31:27.742756: step 1500, loss = 3.215776 (70.7 examples/sec)\
=> 2018-12-16 06:32:15.131361: step 1600, loss = 4.565809 (67.5 examples/sec)\
=> 2018-12-16 06:33:01.978868: step 1700, loss = 3.419047 (68.3 examples/sec)\
=> 2018-12-16 06:33:49.126344: step 1800, loss = 3.421965 (67.9 examples/sec)\
=> 2018-12-16 06:34:35.712214: step 1900, loss = 2.373595 (68.7 examples/sec)\
=> 2018-12-16 06:35:22.702229: step 2000, loss = 3.905905 (68.1 examples/sec)\
==> accuracy = 0.397291, best accuracy 0.079823\
=> 2018-12-16 06:37:43.380424: step 2100, loss = 2.371839 (68.4 examples/sec)\
=> 2018-12-16 06:38:30.256104: step 2200, loss = 1.813903 (68.3 examples/sec)\
=> 2018-12-16 06:39:16.920992: step 2300, loss = 2.433624 (68.6 examples/sec)\
=> 2018-12-16 06:40:03.176388: step 2400, loss = 1.585503 (69.2 examples/sec)\
=> 2018-12-16 06:40:49.420427: step 2500, loss = 2.046654 (69.2 examples/sec)\
=> 2018-12-16 06:41:35.597210: step 2600, loss = 2.231613 (69.3 examples/sec)\
=> 2018-12-16 06:42:21.874074: step 2700, loss = 1.797746 (69.2 examples/sec)\
=> 2018-12-16 06:43:07.850396: step 2800, loss = 2.827516 (69.6 examples/sec)\
=> 2018-12-16 06:43:53.975913: step 2900, loss = 1.952401 (69.4 examples/sec)\
=> 2018-12-16 06:44:40.191450: step 3000, loss = 1.666661 (69.2 examples/sec)\
==> accuracy = 0.644828, best accuracy 0.397291\
=> 2018-12-16 06:46:59.060507: step 3100, loss = 1.277327 (69.4 examples/sec)\
=> 2018-12-16 06:47:45.233029: step 3200, loss = 1.629350 (69.3 examples/sec)\
=> 2018-12-16 06:48:31.308214: step 3300, loss = 1.665735 (69.5 examples/sec)\
=> 2018-12-16 06:49:17.356071: step 3400, loss = 1.431469 (69.5 examples/sec)\
=> 2018-12-16 06:50:03.880554: step 3500, loss = 1.602035 (68.8 examples/sec)\
=> 2018-12-16 06:50:51.912697: step 3600, loss = 1.062685 (66.6 examples/sec)\
=> 2018-12-16 06:51:38.643217: step 3700, loss = 1.650748 (68.5 examples/sec)\
=> 2018-12-16 06:52:25.391615: step 3800, loss = 2.303443 (68.5 examples/sec)\
=> 2018-12-16 06:53:11.271479: step 3900, loss = 1.357635 (69.8 examples/sec)\
=> 2018-12-16 06:53:55.627050: step 4000, loss = 1.889586 (72.2 examples/sec)\
==> accuracy = 0.711659, best accuracy 0.644828\
=> 2018-12-16 06:56:16.570833: step 4100, loss = 1.313027 (68.0 examples/sec)\
=> 2018-12-16 06:57:03.111210: step 4200, loss = 0.751670 (68.8 examples/sec)\
=> 2018-12-16 06:57:49.301686: step 4300, loss = 2.253299 (69.3 examples/sec)\
=> 2018-12-16 06:58:35.583871: step 4400, loss = 1.783667 (69.2 examples/sec)\
=> 2018-12-16 06:59:21.443449: step 4500, loss = 0.736533 (69.8 examples/sec)\
=> 2018-12-16 07:00:06.941940: step 4600, loss = 1.141112 (70.3 examples/sec)\
=> 2018-12-16 07:00:53.191749: step 4700, loss = 0.934278 (69.2 examples/sec)\
=> 2018-12-16 07:01:39.317666: step 4800, loss = 0.789007 (69.4 examples/sec)\
=> 2018-12-16 07:02:24.228835: step 4900, loss = 1.555343 (71.3 examples/sec)\
=> 2018-12-16 07:03:10.627536: step 5000, loss = 0.898773 (69.0 examples/sec)\
==> accuracy = 0.746094, best accuracy 0.711659\
=> 2018-12-16 07:05:29.801836: step 5100, loss = 0.956294 (68.7 examples/sec)\
=> 2018-12-16 07:06:16.567857: step 5200, loss = 1.091872 (68.4 examples/sec)\
=> 2018-12-16 07:07:01.811007: step 5300, loss = 1.012435 (70.7 examples/sec)\
=> 2018-12-16 07:07:48.475752: step 5400, loss = 0.489836 (68.6 examples/sec)\
=> 2018-12-16 07:08:33.022299: step 5500, loss = 0.679983 (71.8 examples/sec)\
=> 2018-12-16 07:09:19.934379: step 5600, loss = 0.893520 (68.2 examples/sec)\
=> 2018-12-16 07:10:04.635188: step 5700, loss = 1.242797 (71.6 examples/sec)\
=> 2018-12-16 07:10:51.281172: step 5800, loss = 2.452408 (68.6 examples/sec)\
=> 2018-12-16 07:11:36.524521: step 5900, loss = 1.157369 (70.7 examples/sec)\
=> 2018-12-16 07:12:23.046576: step 6000, loss = 1.721411 (68.8 examples/sec)\
==> accuracy = 0.809868, best accuracy 0.746094\
=> 2018-12-16 07:14:43.340201: step 6100, loss = 1.056739 (69.3 examples/sec)\
=> 2018-12-16 07:15:28.036084: step 6200, loss = 0.694589 (71.6 examples/sec)\
=> 2018-12-16 07:16:14.981760: step 6300, loss = 1.104462 (68.2 examples/sec)\
=> 2018-12-16 07:17:01.770205: step 6400, loss = 0.716188 (68.4 examples/sec)\
=> 2018-12-16 07:17:48.385257: step 6500, loss = 0.942581 (68.7 examples/sec)\
=> 2018-12-16 07:18:34.879829: step 6600, loss = 0.882159 (68.8 examples/sec)\
=> 2018-12-16 07:19:21.651242: step 6700, loss = 1.078793 (68.4 examples/sec)\
=> 2018-12-16 07:20:08.286392: step 6800, loss = 0.562531 (68.6 examples/sec)\
=> 2018-12-16 07:20:55.137472: step 6900, loss = 0.647254 (68.3 examples/sec)\
=> 2018-12-16 07:21:40.766703: step 7000, loss = 0.864040 (70.1 examples/sec)\
==> accuracy = 0.819845, best accuracy 0.809868\
=> 2018-12-16 07:23:59.352951: step 7100, loss = 0.271859 (71.8 examples/sec)\
=> 2018-12-16 07:24:43.984642: step 7200, loss = 0.979068 (71.7 examples/sec)\
=> 2018-12-16 07:25:28.640271: step 7300, loss = 1.523268 (71.7 examples/sec)\
=> 2018-12-16 07:26:13.374433: step 7400, loss = 1.482918 (71.5 examples/sec)\
=> 2018-12-16 07:26:58.374991: step 7500, loss = 1.132236 (71.1 examples/sec)\
=> 2018-12-16 07:27:42.957325: step 7600, loss = 0.480187 (71.8 examples/sec)\
=> 2018-12-16 07:28:27.473578: step 7700, loss = 0.771609 (71.9 examples/sec)\
=> 2018-12-16 07:29:11.901010: step 7800, loss = 1.492113 (72.0 examples/sec)\
=> 2018-12-16 07:29:56.263197: step 7900, loss = 0.312705 (72.1 examples/sec)\
=> 2018-12-16 07:30:40.703222: step 8000, loss = 0.442074 (72.0 examples/sec)\
==> accuracy = 0.837891, best accuracy 0.819845\
=> 2018-12-16 07:32:59.875019: step 8100, loss = 0.397064 (72.3 examples/sec)\
=> 2018-12-16 07:33:44.302607: step 8200, loss = 0.387942 (72.0 examples/sec)\
=> 2018-12-16 07:34:28.667364: step 8300, loss = 0.496289 (72.1 examples/sec)\
=> 2018-12-16 07:35:12.931702: step 8400, loss = 1.156359 (72.3 examples/sec)\
=> 2018-12-16 07:35:57.225476: step 8500, loss = 0.227380 (72.3 examples/sec)\
=> 2018-12-16 07:36:41.746690: step 8600, loss = 0.487444 (71.9 examples/sec)\
=> 2018-12-16 07:37:26.389655: step 8700, loss = 1.774476 (71.7 examples/sec)\
=> 2018-12-16 07:38:10.581830: step 8800, loss = 1.579779 (72.4 examples/sec)\
=> 2018-12-16 07:38:54.746375: step 8900, loss = 0.699438 (72.5 examples/sec)\
=> 2018-12-16 07:39:39.042292: step 9000, loss = 0.598417 (72.3 examples/sec)\
==> accuracy = 0.842604, best accuracy 0.837891\
=> 2018-12-16 07:41:56.406694: step 9100, loss = 0.724583 (72.2 examples/sec)\
=> 2018-12-16 07:42:40.791229: step 9200, loss = 1.440342 (72.1 examples/sec)\
=> 2018-12-16 07:43:24.870167: step 9300, loss = 1.863581 (72.6 examples/sec)\
=> 2018-12-16 07:44:09.012606: step 9400, loss = 0.353354 (72.5 examples/sec)\
=> 2018-12-16 07:44:53.077821: step 9500, loss = 0.607032 (72.6 examples/sec)\
=> 2018-12-16 07:45:37.158510: step 9600, loss = 0.402449 (72.6 examples/sec)\
=> 2018-12-16 07:46:21.259702: step 9700, loss = 0.855497 (72.6 examples/sec)\
=> 2018-12-16 07:47:05.555761: step 9800, loss = 0.358511 (72.3 examples/sec)\
=> 2018-12-16 07:47:49.943806: step 9900, loss = 0.413619 (72.1 examples/sec)\
=> 2018-12-16 07:48:33.929847: step 10000, loss = 0.650935 (72.8 examples/sec)\
==> accuracy = 0.867230, best accuracy 0.842604\
"


