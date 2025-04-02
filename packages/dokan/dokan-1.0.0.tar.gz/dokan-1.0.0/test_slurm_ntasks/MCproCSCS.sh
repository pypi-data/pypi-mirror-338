#!/bin/bash -l

export OMP_NUM_THREADS=1

aliasHJ161007922RRapro=HJ161007922RRapro

let n=512;
let k=$1;
let k=k-1;

i=`expr $n '*' $k + $SLURM_LOCALID '+' 1`
../NNLOJET -run $aliasHJ161007922RRapro.run -iseed ${i} > $aliasHJ161007922RRapro${i}.slog
