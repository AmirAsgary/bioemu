from bioemu.sample import main as sample

# should be ''' 'mhc_seq'.replace('/', '') + peptide '''
sequence = 'TWAGSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQRMEPRAPWIEQEGPEYWDGETRKVKAHSQTHRVDLGTLRGYYNQSEAGSHTVQRMYGCDVGSDWRFLRGYHQYAYDGKDYIALKEDLRSWTAADMAAQTTKHKWEAAHVAEQLRAYLEGTCVEWLRRYLENGKETLQRTILGGGLLVGLLPAV'
id = 'A0201_neg'
num_samples = 20
output_dir = 'test/A0201_neg'
batch_size_100 = 20
# absolute or relative path to outdir/alphafold
cache_embeds_dir = '/home/amir/amir/ParseFold/PMGen/outputs/bioemu_2/alphafold'
filter_samples=True

sample(sequence=sequence,
        id=id,
        num_samples=num_samples,
        output_dir=output_dir,
        batch_size_100=batch_size_100,
        cache_embeds_dir=cache_embeds_dir,
        filter_samples=filter_samples)