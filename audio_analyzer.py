"""
Audio Feature Extraction for Spotify-like Analysis
Extracts audio features similar to Spotify's API from audio files
"""

import librosa
import numpy as np
import soundfile as sf
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class SpotifyAudioAnalyzer:
    def __init__(self, sample_rate=22050):
        self.sample_rate = sample_rate
    
    def analyze_audio_file(self, file_path):
        """
        Extract Spotify-like features from an audio file
        
        Args:
            file_path (str): Path to audio file
            
        Returns:
            dict: Dictionary of extracted features
        """
        try:
            # Load audio file
            y, sr = librosa.load(file_path, sr=self.sample_rate)
            
            # Extract all features
            features = {}
            
            # Basic properties
            features['duration_min'] = len(y) / sr / 60.0
            
            # Tempo and beat tracking
            tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
            features['tempo'] = float(tempo)
            
            # Time signature (estimate based on beat patterns)
            features['time_signature'] = self._estimate_time_signature(beats, sr)
            
            # Key detection
            features['key'] = self._estimate_key(y, sr)
            features['mode'] = self._estimate_mode(y, sr)
            
            # Energy features
            features['energy'] = self._calculate_energy(y)
            features['loudness'] = self._calculate_loudness(y)
            
            # Spectral features
            features['danceability'] = self._calculate_danceability(y, sr, tempo)
            features['valence'] = self._calculate_valence(y, sr)
            features['acousticness'] = self._calculate_acousticness(y, sr)
            features['instrumentalness'] = self._calculate_instrumentalness(y, sr)
            features['liveness'] = self._calculate_liveness(y, sr)
            features['speechiness'] = self._calculate_speechiness(y, sr)
            
            return features
            
        except Exception as e:
            print(f"Error analyzing audio: {e}")
            return None
    
    def _estimate_time_signature(self, beats, sr):
        """Estimate time signature (simplified to 4/4 for most music)"""
        # For simplicity, assume 4/4 time signature
        # In a more advanced implementation, you could analyze beat patterns
        return 4
    
    def _estimate_key(self, y, sr):
        """Estimate musical key using chroma features"""
        try:
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            chroma_mean = np.mean(chroma, axis=1)
            key = np.argmax(chroma_mean)
            return int(key)
        except:
            return 5  # Default to F
    
    def _estimate_mode(self, y, sr):
        """Estimate major (1) or minor (0) mode"""
        try:
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            chroma_mean = np.mean(chroma, axis=1)
            
            # Simple major/minor detection based on chord patterns
            major_profile = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
            minor_profile = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
            
            major_corr = np.corrcoef(chroma_mean, major_profile)[0, 1]
            minor_corr = np.corrcoef(chroma_mean, minor_profile)[0, 1]
            
            return 1 if major_corr > minor_corr else 0
        except:
            return 1  # Default to major
    
    def _calculate_energy(self, y):
        """Calculate energy as RMS of the signal"""
        rms = librosa.feature.rms(y=y)[0]
        energy = np.mean(rms)
        return float(np.clip(energy * 10, 0, 1))  # Scale to 0-1
    
    def _calculate_loudness(self, y):
        """Calculate loudness in dB"""
        rms = np.sqrt(np.mean(y**2))
        if rms > 0:
            loudness = 20 * np.log10(rms)
            return float(np.clip(loudness, -30, 5))  # Clip to reasonable range
        return -30.0
    
    def _calculate_danceability(self, y, sr, tempo):
        """Calculate danceability based on rhythm and tempo"""
        try:
            # Beat strength and regularity
            onset_envelope = librosa.onset.onset_strength(y=y, sr=sr)
            beat_strength = np.mean(onset_envelope)
            
            # Tempo factor (songs around 120 BPM are more danceable)
            tempo_factor = 1 - abs(tempo - 120) / 120
            tempo_factor = max(0, tempo_factor)
            
            # Rhythm regularity
            beats = librosa.beat.beat_track(y=y, sr=sr)[1]
            if len(beats) > 1:
                beat_intervals = np.diff(beats)
                rhythm_regularity = 1 - (np.std(beat_intervals) / np.mean(beat_intervals))
                rhythm_regularity = max(0, rhythm_regularity)
            else:
                rhythm_regularity = 0.5
            
            danceability = (beat_strength * 0.4 + tempo_factor * 0.3 + rhythm_regularity * 0.3)
            return float(np.clip(danceability, 0, 1))
        except:
            return 0.5
    
    def _calculate_valence(self, y, sr):
        """Calculate valence (musical positivity) using spectral features"""
        try:
            # Use spectral centroid and chroma features
            spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            
            # Higher spectral centroid often indicates brighter, happier sound
            brightness = np.mean(spectral_centroid) / (sr / 2)
            
            # Major vs minor tendency from chroma
            chroma_var = np.var(chroma, axis=1)
            harmony_complexity = np.mean(chroma_var)
            
            valence = (brightness * 0.6 + (1 - harmony_complexity) * 0.4)
            return float(np.clip(valence, 0, 1))
        except:
            return 0.5
    
    def _calculate_acousticness(self, y, sr):
        """Calculate acousticness (likelihood of being acoustic)"""
        try:
            # Use spectral features to detect acoustic vs electric instruments
            spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
            spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            
            # Acoustic instruments typically have different spectral characteristics
            rolloff_mean = np.mean(spectral_rolloff) / (sr / 2)
            centroid_mean = np.mean(spectral_centroid) / (sr / 2)
            
            # Lower rolloff and centroid often indicate more acoustic sound
            acousticness = 1 - (rolloff_mean * 0.5 + centroid_mean * 0.5)
            return float(np.clip(acousticness, 0, 1))
        except:
            return 0.5
    
    def _calculate_instrumentalness(self, y, sr):
        """Calculate instrumentalness (likelihood of no vocals)"""
        try:
            # Detect vocal-like frequencies and patterns
            # Vocals typically appear in 85-255 Hz (fundamental) and harmonics
            spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            
            # Vocal detection based on spectral characteristics
            vocal_range_energy = np.mean(mfccs[1:4])  # MFCC coefficients related to vocal tract
            spectral_stability = 1 - np.std(spectral_centroid) / np.mean(spectral_centroid)
            
            # Higher instrumentalness if less vocal-like characteristics
            instrumentalness = 1 - abs(vocal_range_energy) * 0.1
            return float(np.clip(instrumentalness, 0, 1))
        except:
            return 0.5
    
    def _calculate_liveness(self, y, sr):
        """Calculate liveness (likelihood of live performance)"""
        try:
            # Live recordings often have more ambient noise and reverb
            # Use spectral features and dynamics
            spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
            rms = librosa.feature.rms(y=y)[0]
            
            # Live performances often have more spectral bandwidth variation
            bandwidth_var = np.var(spectral_bandwidth)
            dynamics_var = np.var(rms)
            
            liveness = (bandwidth_var + dynamics_var) * 0.1
            return float(np.clip(liveness, 0, 1))
        except:
            return 0.1
    
    def _calculate_speechiness(self, y, sr):
        """Calculate speechiness (likelihood of spoken words)"""
        try:
            # Speech has different spectral characteristics than music
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
            
            # Speech typically has specific MFCC patterns
            speech_mfcc_pattern = np.mean(np.abs(mfccs[1:5]), axis=0)
            speech_indicator = np.mean(speech_mfcc_pattern)
            
            speechiness = speech_indicator * 0.1
            return float(np.clip(speechiness, 0, 1))
        except:
            return 0.05

def analyze_default_sample():
    """Analyze the default sample file"""
    analyzer = SpotifyAudioAnalyzer()
    
    # Check if default sample exists
    import os
    if os.path.exists('skeletononthebeat.wav'):
        print("Analyzing default sample: skeletononthebeat.wav")
        features = analyzer.analyze_audio_file('skeletononthebeat.wav')
        if features:
            print("\nExtracted features:")
            for key, value in features.items():
                if isinstance(value, float):
                    print(f"{key}: {value:.3f}")
                else:
                    print(f"{key}: {value}")
            return features
    else:
        print("Default sample 'skeletononthebeat.wav' not found")
    return None

if __name__ == "__main__":
    analyze_default_sample()
