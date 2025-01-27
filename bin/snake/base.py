import glob
import os
import sqlite3
import datetime


db_loc = '/data6/bio/TFM/asshole/db.sqlite3'

def save_to_db(task_id, rule_name, in_list, out_list, status ):
    
    save_str_wc = "INSERT INTO explorer_snakeruleresult VALUES (null, '{date_time}', '{task_id}', '{rule_name}', '{in_list}','{out_list}', '{status}');"
    save_str = save_str_wc.format(date_time=datetime.datetime.now(),
task_id=task_id, rule_name=rule_name, in_list=in_list, out_list=out_list, status=status)
    
    print(save_str)
    
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()
    c.execute(save_str)
    conn.commit()
    conn.close()
    
    
snakefiles = './'
results    = '../../results/'

include: results + 'metaphlan2/metaphlan2.py'
include: results + 'megahit/megahit_cross.py'
include: results + 'bwa/bwa.py'
include: results + 'centrifuge/centrifuge.py'
include: results + 'anvio/anvio.py'
include: results + 'trimmomatic/trimmomatic.py'
include: results + 'count/count.py'
include: results + 'fastqc/fastqc.py'
include: results + 'blastn/blastn.py'
include: results + 'metawrap_classify_bins/metawrap_classify_bins.py'
include: results + 'bbmap/bbmap.py'
include: results + 'remove_human_bbmap/remove_human_bbmap.py'
include: results + 'metabat2/metabat2.py'
include: results + 'checkm/checkm.py'
include: results + 'strain_finder/strain_finder.py'
include: results + 'cat_bat/cat_bat.py'
include: results + 'maxbin2/maxbin2.py'
include: results + 'dada2/dada2.py'
include: results + 'coverage/profile.py'
include: results + 'multiqc/multiqc.py'



include: snakefiles + "bins.py"


include: snakefiles + "bowtie2.py"
include: snakefiles + "megares.py"
include: snakefiles + "humann2.py"
include: snakefiles + "qiime2.py"
include: snakefiles + "fasta_operations.py"

include: snakefiles + "ariba.py"
include: snakefiles + "prokka.py"

include: snakefiles + "general.py"
include: snakefiles + "preprocess.py"
include: snakefiles + "taxa.py"
include: snakefiles + "download.py"
include: snakefiles + "find_fungi.py"
    
