import unittest
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# Import your modules (adjust paths as needed)
from CLiMB.core.KBound import KBound

class TestKBound(unittest.TestCase):
    
    def setUp(self):
        """Create synthetic datasets and setup for testing"""
        # Create dataset with known clusters
        self.X_blobs, self.y_blobs = make_blobs(
            n_samples=300, 
            centers=3, 
            n_features=3, 
            random_state=42
        )
        
        # Standardize datasets
        self.scaler = StandardScaler()
        self.X_blobs_scaled = self.scaler.fit_transform(self.X_blobs)
        
        # Create seed points from known clusters
        self.seed_points = np.array([
            self.X_blobs[self.y_blobs == 0].mean(axis=0),
            self.X_blobs[self.y_blobs == 1].mean(axis=0),
            self.X_blobs[self.y_blobs == 2].mean(axis=0)
        ])
        
        # Create scaled seed points
        self.seed_points_scaled = self.scaler.transform(self.seed_points)
    
    def test_initialization(self):
        """Test proper initialization of KBound"""
        # Test with default parameters
        kbound = KBound(self.seed_points_scaled)
        self.assertEqual(kbound.k, len(self.seed_points_scaled))
        self.assertTrue(np.array_equal(kbound.initial_centroids, self.seed_points_scaled))
        self.assertEqual(kbound.radial_threshold, 1.0)
        self.assertEqual(kbound.convergence_tolerance, 0.001)
        
        # Test with custom parameters
        custom_kbound = KBound(
            self.seed_points_scaled, 
            radial_threshold=2.0,
            convergence_tolerance=0.01
        )
        self.assertEqual(custom_kbound.radial_threshold, 2.0)
        self.assertEqual(custom_kbound.convergence_tolerance, 0.01)
    
    def test_fit(self):
        """Test fitting on blob dataset"""
        kbound = KBound(self.seed_points_scaled)
        kbound.fit(self.X_blobs_scaled)
        
        # Check that attributes are properly set after fitting
        self.assertIsNotNone(kbound.labels_)
        self.assertIsNotNone(kbound.centroids_)
        self.assertIsNotNone(kbound.cluster_distances_)
        
        # Check number of clusters
        self.assertEqual(len(np.unique(kbound.labels_[kbound.labels_ >= 0])), len(self.seed_points_scaled))
        
        # Check centroids shape
        self.assertEqual(kbound.centroids_.shape, self.seed_points_scaled.shape)
    
    def test_fit_predict(self):
        """Test fit_predict method"""
        kbound = KBound(self.seed_points_scaled)
        labels = kbound.fit_predict(self.X_blobs_scaled)
        
        # Check that labels match the expected length
        self.assertEqual(len(labels), len(self.X_blobs_scaled))
        
        # Check that the number of unique labels (excluding noise) matches k
        self.assertEqual(len(np.unique(labels[labels >= 0])), len(self.seed_points_scaled))
        
        # Check that fit_predict labels match labels_ attribute
        self.assertTrue(np.array_equal(labels, kbound.labels_))
    
    def test_predict(self):
        """Test predict method on new data"""
        kbound = KBound(self.seed_points_scaled)
        kbound.fit(self.X_blobs_scaled)
        
        # Create some new test data points
        test_points = np.array([
            self.X_blobs_scaled[0],  # Should be assigned to its original cluster
            self.X_blobs_scaled[100],  # Should be assigned to its original cluster
            self.X_blobs_scaled[200],  # Should be assigned to its original cluster
            [10, 10, 10]  # Should be noise (-1)
        ])
        
        predicted_labels = kbound.predict(test_points)
        
        # Check that we have predictions for all test points
        self.assertEqual(len(predicted_labels), len(test_points))
        
        # Check that far away points are labeled as noise (-1)
        self.assertEqual(predicted_labels[3], -1)
    
    def test_convergence(self):
        """Test convergence of centroid updates"""
        # Create a KBound instance with a very tight convergence tolerance
        kbound = KBound(
            self.seed_points_scaled,
            convergence_tolerance=1e-6
        )
        
        # Fit the model and get the number of iterations
        kbound.fit(self.X_blobs_scaled)
        iterations = kbound.iterations_
        
        # Fit again with a looser convergence tolerance
        kbound_loose = KBound(
            self.seed_points_scaled,
            convergence_tolerance=0.1
        )
        kbound_loose.fit(self.X_blobs_scaled)
        loose_iterations = kbound_loose.iterations_
        
        # Check that looser tolerance requires fewer iterations
        self.assertLessEqual(loose_iterations, iterations)
    
    def test_radial_threshold_effect(self):
        """Test effect of radial threshold on point assignment"""
        # First with default threshold
        kbound_default = KBound(self.seed_points_scaled)
        kbound_default.fit(self.X_blobs_scaled)
        default_assigned = np.sum(kbound_default.labels_ >= 0)
        
        # Then with a very small threshold (should assign fewer points)
        kbound_small = KBound(self.seed_points_scaled, radial_threshold=0.1)
        kbound_small.fit(self.X_blobs_scaled)
        small_assigned = np.sum(kbound_small.labels_ >= 0)
        
        # Then with a very large threshold (should assign more points)
        kbound_large = KBound(self.seed_points_scaled, radial_threshold=10.0)
        kbound_large.fit(self.X_blobs_scaled)
        large_assigned = np.sum(kbound_large.labels_ >= 0)
        
        # Verify that threshold has the expected effect
        self.assertLessEqual(small_assigned, default_assigned)
        self.assertGreaterEqual(large_assigned, default_assigned)

if __name__ == '__main__':
    unittest.main()
